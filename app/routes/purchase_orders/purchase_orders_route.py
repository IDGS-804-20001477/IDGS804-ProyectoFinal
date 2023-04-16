from flask import Blueprint, render_template, request, redirect, url_for
from ...models.purchase_order import Purchase_Order
from ...controllers.purchase_order_controller import getBuyOrders, getBuyOrderById, insertBuyOrder, updateBuyOrder, deleteBuyOrder

purchase_orders = Blueprint('purchase_orders', __name__, url_prefix='/admin/purchase-orders')


@purchase_orders.route('/purchase-orders-index')
def index():
    buyOrders = getBuyOrders(1)
    return render_template('/admin/purchase-orders/index_purchase_orders.html', buyOrders=buyOrders)


@purchase_orders.route('/purchase-orders-insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        total = request.form.get('txtTotal')
        provider_id = request.form.get('cmbProvider')
        purchase_order_detail = request.form.get('tblDetails')
        purchase_order = Purchase_Order(0, '', total, provider_id, purchase_order_detail)
        insertBuyOrder(purchase_order)

        return redirect(url_for('purchase_orders.index'))

    return render_template('/admin/purchase-orders/insert_purchase_order.html')


@purchase_orders.route('/purchase-orders-update', methods=['GET', 'POST'])
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getBuyOrderById(id)
        return render_template('/admin/purchase-orders/update_purchase_order.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        reference_number = request.form.get('txtReferenceNumber')
        total = request.form.get('txtTotal')
        provider_id = request.form.get('cmbProvider')
        purchase_order_detail = request.form.get('tblDetails')
        purchase_order = Purchase_Order(id, reference_number, total, provider_id, purchase_order_detail)
        updateBuyOrder(purchase_order)
        return redirect(url_for('purchase_orders.index'))

@purchase_orders.route('/purchase-orders-delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getBuyOrderById(id)
        return render_template('/admin/purchase-orders/delete_purchase_order.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteBuyOrder(id)
        return redirect(url_for('purchase_orders.index'))
