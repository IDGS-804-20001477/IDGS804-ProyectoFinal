from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_security import login_required, current_user
from flask_security.decorators import roles_accepted, roles_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about_us')
def about_us():
    return render_template('about_us.html')

@main.route('/contact', methods=['POST', 'GET'])
def contact():
    current_app.config['WTF_CSRF_ENABLED'] = False
    if request.method == 'POST':
        flash('¡Gracias por contactarnos!')
        return render_template('contact.html')
    else:
        return render_template('contact.html')

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