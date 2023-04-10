from flask import Blueprint, render_template, request, redirect, url_for
from ...models.purchase_order import Buy_Order
from ...models.purchase_order_detail import Buy_Order_Detail
from ...controllers.purchase_order_controller import getBuyOrders, getBuyOrderById, insertBuyOrder, updateBuyOrder, deleteBuyOrder

buyOrders = Blueprint('buyOrders', __name__, url_prefix='/buyOrders')


@buyOrders.route('/buyOrders-index')
def index():
    buyOrders = getBuyOrders(1)
    return render_template('/buyOrders/index_buyOrders.html', buyOrders=buyOrders)


@buyOrders.route('/buyOrders-insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        total = request.form.get('txtTotal')
        provider_id = request.form.get('cmbProvider')
        quantity = request.form.get('txtQuantity')
        price = request.form.get('txtPrice')
        feedstock_id = request.form.get('cmbFeedstock_id')
        buyOrder = Buy_Order(0, total, provider_id)
        buyOrder = Buy_Order_Detail(0, quantity, price, feedstock_id)
        insertBuyOrder(buyOrder)

        return redirect(url_for('buyOrders.index'))

    return render_template('/buyOrders/insert-buyOrder.html')


@buyOrders.route('/buyOrders-update', methods=['GET', 'POST'])
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getBuyOrderById(id)
        return render_template('/buyOrders/update_BuyOrder.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        total = request.form.get('txtTotal')
        provider_id = request.form.get('cmbProvider')
        quantity = request.form.get('txtQuantity')
        price = request.form.get('txtPrice')
        feedstock_id = request.form.get('cmbFeedstock_id')
        buyOrder = Buy_Order(id, total, provider_id)
        buyOrder = Buy_Order_Detail(id, quantity, price, feedstock_id)

        updateBuyOrder(buyOrder)
        return redirect(url_for('buyOrders.index'))

@buyOrders.route('/buyOrders-delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getBuyOrderById(id)
        return render_template('/buyOrders/delete_buyOrder.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteBuyOrder(id)
        return redirect(url_for('buyOrders.index'))
