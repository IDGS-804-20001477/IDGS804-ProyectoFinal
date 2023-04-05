from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_accepted, roles_required


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
@roles_accepted('admin', 'client')
def profile():
    return render_template('profile.html', name=current_user.email)


@main.route('/information')
@login_required
@roles_accepted('admin', 'client')
def information():
    return render_template('information.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')