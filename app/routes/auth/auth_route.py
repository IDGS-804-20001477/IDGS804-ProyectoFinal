from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models.auth import db, User, User_Profile
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security.utils import login_user, logout_user
from flask_security import login_required, current_user
from ... import userDataStore
import logging


auth = Blueprint('auth', __name__, url_prefix='/auth')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@auth.get('/password')
def get_password():
    return generate_password_hash('admin', method='sha256')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'GET'):
        return render_template('/auth/login.html')

    if (request.method == 'POST'):
        email = request.form.get('txtEmail')
        password = request.form.get('txtPassword')
        remember = True if request.form.get('opcRemember') else False
        user = User.query.filter_by(email=email).first()
        print(user.name)

        if (not user or not check_password_hash(user.password, password)):
            flash('EL usuario o contraseña son incorrectos')
            logger.warning('Datos erroneos al ingresar al sistema')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)

        if user.type == 2:
            logger.info('Se ingreso al sistema como cliente: %s',
                        current_user.name)
            return redirect(url_for('main.index'))
        else:
            return redirect(url_for('dashboard.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'GET'):
        return render_template('/auth/register.html')

    if (request.method == 'POST'):
        email = request.form.get('txtEmail')
        name = request.form.get('txtName')
        lastname = request.form.get('txtLastName')
        address = request.form.get('txtAddress')
        phone = request.form.get('txtTel')

        password = request.form.get('txtPassword')
        user = User.query.filter_by(email=email).first()

        if (user):
            flash('El correo ya tiene uso')
            logger.warning('El correo ya esta en uso')
            return redirect(url_for('auth.login'))

        user_created = userDataStore.create_user(name=name, email=email, password=generate_password_hash(
            password, method='sha256'), type=2, active=True, roles=['client'])

        # user_profile = User_Profile(
        #    lastname=lastname, address=address, phone=phone, user_id=user_created.id)

        # db.session.add(user_profile)
        logger.info('Se registro correctamente')
        db.session.commit()
        return redirect(url_for('auth.login'))


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    logger.info('Salio del sistema')
    return redirect(url_for('main.index'))
