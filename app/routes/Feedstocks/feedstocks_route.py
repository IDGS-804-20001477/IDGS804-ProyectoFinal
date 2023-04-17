from flask import Blueprint, render_template, request, redirect, url_for
from ...models.feedstock import Feedstock
from ...controllers.feedstocks_controller import getFeedstocks, getFeedstockById, insertFeedstock, updateFeedstock, deleteFeedstock
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
    if (request.method == 'POST'):
        name = request.form.get('txtName')
        description = request.form.get('txtDescription')
        price = request.form.get('txtPrice')
        provider_id = request.form.get('cmbProvider')
        measurement_unit_id = request.form.get('cmbMeasurement_unit')
        min_value = request.form.get('txtMinValue')
        max_value = request.form.get('txtMaxValue')
        quantity = request.form.get('txtQuantity')
        feedstock = Feedstock(0, name, description, price,
                              provider_id, measurement_unit_id, min_value, max_value, quantity)
        insertFeedstock(feedstock)
        return redirect(url_for('feedstocks.index'))

    return render_template('/admin/feedstocks/insert_feedstock.html')


@feedstocks.route('/feedstocks-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getFeedstockById(id)
        return render_template('/admin/feedstocks/update_feedstock.html', form=response)

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
        feedstock = Feedstock(id, name, description, price,
                              provider_id, measurement_unit_id, min_value, max_value, quantity)
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
