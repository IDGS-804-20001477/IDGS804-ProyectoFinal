from flask import Blueprint, render_template, request, redirect, url_for
from ...models.purchase_order import Purchase_Order
from ...controllers.purchase_order_controller import getPurchaseOrders, getPurchaseOrderById, insertPurchaseOrder, updatePurchaseOrder
from ...controllers.providers_controller import getProvidersForFeedstock
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
import logging

purchase_orders = Blueprint(
    'purchase_orders', __name__, url_prefix='/admin/purchase-orders')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@purchase_orders.route('/purchase-orders-index')
@login_required
@roles_required('admin')
def index():
    purchase_orders_requested = getPurchaseOrders(1)
    purchase_orders_on_the_way = getPurchaseOrders(2)
    purchase_orders_delivered = getPurchaseOrders(3)
    purchase_orders_canceled = getPurchaseOrders(4)
    logger.info('Se muestran las ordenes de compra: %s', current_user.name)
    return render_template('/admin/purchase-orders/index_purchase_order.html', purchase_orders_requested=purchase_orders_requested, purchase_orders_on_the_way=purchase_orders_on_the_way, purchase_orders_delivered=purchase_orders_delivered, purchase_orders_canceled=purchase_orders_canceled)


@purchase_orders.route('/purchase-orders-insert', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def insert():
    providers = getProvidersForFeedstock()
    
    if (request.method == 'POST'):
        data = request.get_json()
        provider_id = int(data['provider_id'])
        total = float(data['total'])
        details = data['array']
        purchase_order = Purchase_Order(0, '', total, provider_id, details)
        print(insertPurchaseOrder(purchase_order))
        logger.info('Se inserta una orden de compra correctamente: %s', current_user.name)
        return redirect(url_for('purchase_orders.index'))

    return render_template('/admin/purchase-orders/insert_purchase_order.html', providers=providers)


@purchase_orders.route('/purchase-orders-see-order', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def see_order():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getPurchaseOrderById(id)
        logger.info('Se muestra la orden de compra por id: %s', current_user.name)
        return render_template('/admin/purchase-orders/see_detail_purchase_order.html', form=response)

    if (request.method == 'POST'):
        return redirect(url_for('purchase_orders.index'))


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
        new_status = int(request.form.get('txtStatus')) + 1
        updatePurchaseOrder(id, new_status)
        logger.info('Se modifica la orden de compra correctamente: %s', current_user.name)
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
        logger.info('Se elimina orden de compra correctamente: %s', current_user.name)
        return redirect(url_for('purchase_orders.index'))
