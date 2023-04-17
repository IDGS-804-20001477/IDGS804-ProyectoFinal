from flask import Blueprint, render_template, request, redirect, url_for
from ...models.purchase_order import Purchase_Order
from ...controllers.purchase_order_controller import getPurchaseOrders, getPurchaseOrderById, insertPurchaseOrder, updatePurchaseOrder
from flask_security import login_required
from flask_security.decorators import roles_required

purchase_orders = Blueprint('purchase_orders', __name__, url_prefix='/admin/purchase-orders')


@purchase_orders.route('/purchase-orders-index')
@login_required
@roles_required('admin')
def index():
    buyOrders = getPurchaseOrders()
    return render_template('/admin/purchase-orders/index_purchase_orders.html', buyOrders=buyOrders)


@purchase_orders.route('/purchase-orders-insert', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def insert():
    if (request.method == 'POST'):
        total = request.form.get('txtTotal')
        provider_id = request.form.get('cmbProvider')
        purchase_order_detail = request.form.get('tblDetails')
        purchase_order = Purchase_Order(0, '', total, provider_id, purchase_order_detail)
        insertPurchaseOrder(purchase_order)
        return redirect(url_for('purchase_orders.index'))

    return render_template('/admin/purchase-orders/insert_purchase_order.html')


@purchase_orders.route('/purchase-orders-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getPurchaseOrderById(id)
        return render_template('/admin/purchase-orders/update_purchase_order.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        new_status = int(request.args.get('status') + 1)
        updatePurchaseOrder(id, new_status)
        return redirect(url_for('purchase_orders.index'))

@purchase_orders.route('/purchase-orders-delete', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getPurchaseOrderById(id)
        return render_template('/admin/purchase-orders/delete_purchase_order.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        updatePurchaseOrder(id, 4)
        return redirect(url_for('purchase_orders.index'))
