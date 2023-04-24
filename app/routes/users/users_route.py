from flask import Blueprint, request, redirect, url_for, render_template, flash
from ...models.auth import User, Role
from ...models.db import db
from ...controllers.users_controllers import getUsers, getUserById, getUserTypes, insertUser, updateUser, deleteUser
from werkzeug.security import generate_password_hash
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from app import userDataStore
import logging

users = Blueprint('users', __name__, url_prefix='/admin/users')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@users.route('/users-index')
@login_required
@roles_required('admin')
def index():
    users = getUsers(1)
    logger.info('Se muestra el usuario: %s', current_user.name)
    return render_template('/admin/users/index_user.html', users=users)


@users.route('/users-insert', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def insert():
    user_types = getUserTypes(1)

    if (request.method == 'POST'):
        email = request.form.get('txtEmail')
        password = request.form.get('txtPassword')
        role = request.form.get('cmbTypes')
        name = request.form.get('txtName')
        lastname = request.form.get('txtLastname')
        address = request.form.get('txtAddress')
        phone = request.form.get('txtPhone')
        # user = User(0, email, generate_password_hash(
        #    password, method='sha256'), type, name, lastname, address, phone)
        # insertUser(user)
        user_found = User.query.filter_by(email=email).all()

        if user_found:
            flash('Ya existe un usuario con este email')
            return redirect(url_for('users.insert'))

        user = userDataStore.create_user(
            email=email,
            password=generate_password_hash(password, method='sha256'),
            type=2 if role == 'client' else 1,
            name=name,
            roles=[role]
        )
        logger.info('Se inserta usuario correctamente: %s', current_user.name)
        db.session.commit()
        return redirect(url_for('users.index'))

    roles = Role.query.all()

    return render_template('/admin/users/insert_user.html', roles=roles)


@users.route('/users-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        user_types = getUserTypes(1)
        user = getUserById(id)
        return render_template('/admin/users/update_user.html', form=user, user_types=user_types)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        email = request.form.get('txtEmail')
        password = request.form.get('txtPassword')
        type = request.form.get('cmbTypes')
        name = request.form.get('txtName')
        lastname = request.form.get('txtLastname')
        address = request.form.get('txtAddress')
        phone = request.form.get('txtPhone')
        # user = User(id, email, generate_password_hash(password, method='sha256'), type, name, lastname, address, phone)
        # updateUser(user)
        logger.info('Se modifica usuario correctamente: %s', current_user.name)
        return redirect(url_for('users.index'))


@users.route('/users-delete', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        user = getUserById(id)
        return render_template('/admin/users/delete_user.html', form=user)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteUser(id)
        logger.info('Se elimina usuario correctamente: %s', current_user.name)
        return redirect(url_for('users.index'))
