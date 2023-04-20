from flask import Blueprint, render_template, request, redirect, url_for
from ...models.feedstock import Feedstock
from ...controllers.feedstocks_controller import getFeedstocks, getFeedstockById, insertFeedstock, updateFeedstock, deleteFeedstock, getFeedstocksByProvider
from ...controllers.providers_controller import getProvidersForFeedstock
from ...controllers.measurement_units_controller import getMeasurementUnits
from flask_security import login_required
from flask_security.decorators import roles_required

feedstocks = Blueprint('feedstocks', __name__, url_prefix='/admin/feedstocks')


@feedstocks.route('/feedstocks-index')
@login_required
@roles_required('admin')
def index():
    feedstocks = getFeedstocks(1)
    return render_template('/admin/feedstocks/index_feedstock.html', feedstocks=feedstocks)


@feedstocks.route('/feedstocks-insert', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def insert():
    providers = getProvidersForFeedstock()
    measurement_units = getMeasurementUnits(1)

    if (request.method == 'POST'):
        name = request.form.get('txtName')
        description = request.form.get('txtDescription')
        price = request.form.get('txtPrice')
        provider_id = request.form.get('cmbProvider')
        measurement_unit_id = request.form.get('cmbMeasurement_unit')
        min_value = request.form.get('txtMinValue')
        max_value = request.form.get('txtMaxValue')
        quantity = request.form.get('txtQuantity')
        feedstock = Feedstock(0, name, description, price, min_value,
                              max_value, measurement_unit_id, provider_id, quantity)
        insertFeedstock(feedstock)
        return redirect(url_for('feedstocks.index'))

    return render_template('/admin/feedstocks/insert_feedstock.html', providers=providers, measurement_units=measurement_units)


@feedstocks.route('/feedstocks-by-provider', methods=['POST'])
@login_required
@roles_required('admin')
def feedstocks_by_provider():
    data = request.get_json()
    provider_id = int(data['id'])
    response = []
    for i in getFeedstocksByProvider(provider_id):
        object_ = {"id": i[0], "name": i[1]}
        response.append(object_)
    return response


@feedstocks.route('/feedstocks-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if (request.method == 'GET'):
        providers = getProvidersForFeedstock()
        measurement_units = getMeasurementUnits(1)
        id = request.args.get('id')
        response = getFeedstockById(id)
        return render_template('/admin/feedstocks/update_feedstock.html', form=response, providers=providers, measurement_units=measurement_units)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        name = request.form.get('txtName')
        description = request.form.get('txtDescription')
        price = request.form.get('txtPrice')
        provider_id = request.form.get('cmbProvider')
        measurement_unit_id = request.form.get('cmbMeasurement_unit')
        min_value = request.form.get('txtMinValue')
        max_value = request.form.get('txtMaxValue')
        quantity = request.form.get('txtQuantity')
        feedstock = Feedstock(id, name, description, price, min_value,
                              max_value, measurement_unit_id, provider_id, quantity)
        updateFeedstock(feedstock)
        return redirect(url_for('feedstocks.index'))


@feedstocks.route('/feedstocks-delete', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getFeedstockById(id)
        return render_template('/admin/feedstocks/delete_feedstock.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteFeedstock(id)
        return redirect(url_for('feedstocks.index'))
