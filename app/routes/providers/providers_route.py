from flask import Blueprint, render_template

providers = Blueprint('providers', __name__)


@providers.route('providers-index')
def index():
    return render_template('providers_index')
