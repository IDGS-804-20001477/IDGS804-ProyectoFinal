from flask import Blueprint, request, redirect, url_for, render_template
from ...models.sale_order import Sale_Order
from ...controllers.sales_orders_controller import getSalesOrders, getSaleOrderById, insertSaleOrder, updateSaleOrder
from ...models.sale_order import Sale_Order

sale_orders = Blueprint('sale_orders', __name__, url_prefix='/admin/sale-orders')


@sale_orders.route('/sale-orders-index')
def index():
    sale_orders = getSalesOrders()
    return render_template('/admin/sale-orders/index_sale_order.html', sale_orders=sale_orders)


@sale_orders.route('/shopping-cart-insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        client_id = request.cookies.get('user_id')
        total = request.form.get('txtTotal')
        sale_order_detail = request.form.get(
            '<<nombre del componente que tendrá el detalle>>')
        sale_order = Sale_Order(0, '', total, 0, client_id, sale_order_detail)
        insertSaleOrder(sale_order)
        redirect(url_for('main.index'))

    return render_template('/admin/sale-orders/insert_sale_order.html')


@sale_orders.route('/sale-orders-update', methods=['GET', 'POST'])
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        sale_order = getSaleOrderById(id)
        return render_template('/admin/sale-orders/update_sale_order.html', sale_order=sale_order)
    
    if(request.method == 'POST'):
        new_status = int(request.args.get('status') + 1)
        id = request.form.get('txtId')
        updateSaleOrder(id, new_status)
        return redirect(url_for('sale_orders.index'))


@sale_orders.route('/sale-orders-delete', methods=['GET', 'POST'])
def delete():
    if(request.method == 'GET'):
        id = request.args.get('id')
        sale_order = getSaleOrderById(id)
        return render_template('/admin/sale-orders/delete_sale_order.html', sale_order=sale_order)
    
    if(request.method == 'POST'):
        new_status = 6
        id = request.form.get('txtId')
        updateSaleOrder(id, new_status)
        return redirect(url_for('sale_orders.index'))