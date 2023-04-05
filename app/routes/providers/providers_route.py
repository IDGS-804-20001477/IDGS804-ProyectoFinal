from flask import Blueprint, render_template, request, redirect, url_for
from ...controllers.providers_controller import getProviders, getProviderById, deleteProvider, insertProvider, updateProvider
from ...models.provider import Provider

providers = Blueprint('providers', __name__, url_prefix='/providers')


@providers.route('/providers-index')
def index():
    providers = getProviders(1)
    return render_template('/providers/index_provider.html', providers=providers)


@providers.route('/providers-insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        business_name = request.form.get('txtBusinessName')
        contact_name = request.form.get('txtContactName')
        contact_email = request.form.get('txtContactEmail')
        contact_phone = request.form.get('txtContactPhone')
        address = request.form.get('txtAddress')
        provider = Provider(0, business_name, contact_name,
                            contact_email, contact_phone, address)
        insertProvider(provider)
        return redirect(url_for('providers.index'))

    return render_template('/providers/insert_provider.html')


@providers.route('/providers-update', methods=['GET', 'POST'])
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProviderById(id)
        return render_template('/providers/update_provider.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        business_name = request.form.get('txtBusinessName')
        contact_name = request.form.get('txtContactName')
        contact_email = request.form.get('txtContactEmail')
        contact_phone = request.form.get('txtContactPhone')
        address = request.form.get('txtAddress')
        provider = Provider(id, business_name, contact_name,
                            contact_email, contact_phone, address)
        updateProvider(provider)
        return redirect(url_for('providers.index'))


@providers.route('/providers-delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProviderById(id)
        return render_template('/providers/delete_provider.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteProvider(id)
        return redirect(url_for('providers.index'))
