from flask import Blueprint, render_template, request, redirect, url_for
from ...controllers.providers_controller import getProviders, getProvider, deleteProvider, insertProvider, updateProvider
from ...models.provider import Provider
from ...models.forms import ProviderForm

providers = Blueprint('providers', __name__)


@providers.route('/providers-index')
def index():
    return render_template('provider_index')


@providers.route('/providers-insert', methods=['GET', 'POST'])
def insert():
    create_form = ProviderForm(request.form)

    if (request.method == 'POST'):
        provider = Provider(0, create_form.business_name.data, create_form.contact_name.data,
                            create_form.contact_email.data, create_form.contact_phone.data, create_form.address.data)
        insertProvider(provider)
        return redirect(url_for('providers.index'))

    return render_template('insert_provider.html', form=create_form)


@providers.route('/providers-update', methods=['GET', 'POST'])
def update():
    create_form = ProviderForm(request.form)

    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProvider(id, create_form)
        return render_template('update_provider.html', form=response)

    if (request.method == 'POST'):
        provider = Provider(create_form.id.data, create_form.business_name.data, create_form.contact_name.data,
                            create_form.contact_email.data, create_form.contact_phone.data, create_form.address.data)
        updateProvider(provider)
        return redirect(url_for('providers.index'))


@providers.route('/providers-delete', methods=['GET', 'POST'])
def delete():
    create_form = ProviderForm(request.form)

    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProvider(id, create_form)
        return render_template('delete_provider.html', form=response)

    if (request.method == 'POST'):
        deleteProvider(create_form.id.data)
        return redirect(url_for('providers.index'))
