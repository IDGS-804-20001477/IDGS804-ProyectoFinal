from flask import Blueprint, request, redirect, url_for, render_template
from ...models.user import User
from ...controllers.users_controllers import getUsers, getUserById, getUserTypes, insertUser, updateUser, deleteUser
from werkzeug.security import generate_password_hash
from flask_security import login_required
from flask_security.decorators import roles_required

users = Blueprint('users', __name__, url_prefix='/admin/users')


@users.route('/users-index')
@login_required
@roles_required('admin')
def index():
    users = getUsers(1)
    return render_template('/admin/users/index_user.html', users=users)


@users.route('/users-insert', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def insert():
    user_types = getUserTypes(1)

    if (request.method == 'POST'):
        email = request.form.get('txtEmail')
        password = request.form.get('txtPassword')
        type = request.form.get('cmbTypes')
        name = request.form.get('txtName')
        lastname = request.form.get('txtLastname')
        address = request.form.get('txtAddress')
        phone = request.form.get('txtPhone')
        user = User(0, email, generate_password_hash(
            password, method='sha256'), type, name, lastname, address, phone)
        insertUser(user)
        return redirect(url_for('users.index'))

    return render_template('/admin/users/insert_user.html', user_types=user_types)


@users.route('/users-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if(request.method == 'GET'):
        id = request.args.get('id')
        user_types = getUserTypes(1)
        user = getUserById(id)
        return render_template('/admin/users/update_user.html', form=user, user_types=user_types)
    
    if(request.method == 'POST'):
        id = request.form.get('txtId')
        email = request.form.get('txtEmail')
        password = request.form.get('txtPassword')
        type = request.form.get('cmbTypes')
        name = request.form.get('txtName')
        lastname = request.form.get('txtLastname')
        address = request.form.get('txtAddress')
        phone = request.form.get('txtPhone')
        user = User(id, email, generate_password_hash(password, method='sha256'), type, name, lastname, address, phone)
        updateUser(user)
        return redirect(url_for('users.index'))
    

@users.route('/users-delete', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def delete():
    if(request.method == 'GET'):
        id = request.args.get('id')
        user = getUserById(id)
        return render_template('/admin/users/delete_user.html', form=user)
    
    if(request.method == 'POST'):
        id = request.form.get('txtId')
        deleteUser(id)
        return redirect(url_for('users.index'))