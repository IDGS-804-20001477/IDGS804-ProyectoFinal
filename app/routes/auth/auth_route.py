from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models.auth import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security.utils import login_user, logout_user
from flask_security import login_required
from ... import userDataStore


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'GET'):
        return render_template('/auth/login.html')

    if (request.method == 'POST'):
        email = request.form.get('txtEmail')
        password = request.form.get('txtPassword')
        remember = True if request.form.get('opcRemember') else False
        user = User.query.filter_by(email=email).first()

        if (not user or not check_password_hash(user.password, password)):
            flash('EL usuario o contraseña son incorrectos')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'GET'):
        return render_template('/auth/register.html')

    if (request.method == 'POST'):
        email = request.form.get('txtEmail')
        password = request.form.get('txtPassword')
        user = User.query.filter_by(email=email).first()

        if (user):
            flash('El correo ya tiene uso')
            return redirect(url_for('auth.login'))

        userDataStore.create_user(email=email, password=generate_password_hash(password, method='sha256'), type=2)
        db.session.commit()
        return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))