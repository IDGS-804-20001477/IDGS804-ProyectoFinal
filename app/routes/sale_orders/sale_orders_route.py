from flask import Blueprint, request, redirect, url_for, render_template
from ...models.sale_order import Sale_Order
from ...controllers.sales_orders_controller import getSalesOrders, getSaleOrderById, insertSaleOrder, updateSaleOrder
from ...models.sale_order import Sale_Order
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
import logging

sale_orders = Blueprint('sale_orders', __name__,
                        url_prefix='/admin/sale-orders')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@sale_orders.route('/sale-orders-index')
@login_required
@roles_required('admin')
def index():
    sale_orders_requested = getSalesOrders(1)
    sale_orders_elaborating = getSalesOrders(2)
    sale_orders_packing = getSalesOrders(3)
    sale_orders_sending = getSalesOrders(4)
    sale_orders_delivered = getSalesOrders(5)
    sale_orders_canceled = getSalesOrders(6)
    logger.info('Se muestra las ordenes de venta: %s', current_user.name)
    return render_template('/admin/sale-orders/index_sale_order.html', sale_orders_requested=sale_orders_requested, sale_orders_elaborating=sale_orders_elaborating, sale_orders_packing=sale_orders_packing, sale_orders_sending=sale_orders_sending, sale_orders_delivered=sale_orders_delivered, sale_orders_canceled=sale_orders_canceled)


@sale_orders.route('/shopping-cart-insert', methods=['GET', 'POST'])
@login_required
@roles_required('client')
def insert():
    if (request.method == 'POST'):
        client_id = request.cookies.get('user_id')
        total = request.form.get('txtTotal')
        sale_order_detail = request.form.get(
            '<<nombre del componente que tendrá el detalle>>')
        sale_order = Sale_Order(0, '', total, 0, client_id, sale_order_detail)
        insertSaleOrder(sale_order)
        logger.info('Se inserta orden de venta correctamente: %s', current_user.name)
        redirect(url_for('main.index'))

    return render_template('/admin/sale-orders/insert_sale_order.html')


@sale_orders.route('/sale-orders-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        sale_order = getSaleOrderById(id)
        return render_template('/admin/sale-orders/update_sale_order.html', form=sale_order)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        new_status = int(request.form.get('txtStatus')) + 1
        print(updateSaleOrder(id, new_status))
        logger.info('Se modifica orden de venta correctamente: %s', current_user.name)
        return redirect(url_for('sale_orders.index'))


@sale_orders.route('/sale-orders-delete', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        sale_order = getSaleOrderById(id)
        return render_template('/admin/sale-orders/delete_sale_order.html', form=sale_order)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        updateSaleOrder(id, 6)
        logger.info('Se elimina orden de venta correctamente: %s', current_user.name)
        return redirect(url_for('sale_orders.index'))


@sale_orders.route('/sale-orders-see-detail', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def see_order():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getSaleOrderById(id)
        logger.info('Se muestran los detalles de la orden de venta: %s', current_user.name)
        return render_template('/admin/sale-orders/see_detail_sale_order.html', form=response)

    if (request.method == 'POST'):
        return redirect(url_for('sale_orders.index'))
