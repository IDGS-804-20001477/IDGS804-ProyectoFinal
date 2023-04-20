from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from flask_security import login_required, current_user
from flask_security.decorators import roles_accepted, roles_required
from ...models.sale_order import SaleOrder, SaleOrdeDetail
from ...models.db import db
from ...utils.mercado_pago import sdk, get_preference_body
from ...models.product import ProductModel
from datetime import date
import uuid

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about_us')
def about_us():
    return render_template('about_us.html')


@main.route('/contact', methods=['POST', 'GET'])
def contact():
    current_app.config['WTF_CSRF_ENABLED'] = False
    if request.method == 'POST':
        flash('¡Gracias por contactarnos!')
        return render_template('contact.html')
    else:
        return render_template('contact.html')


@main.get('/products')
def get_products():
    products = ProductModel.query.filter_by(status=1).all()
    return render_template('products/index.html', products=products)


@main.get('/products/<int:product_id>')
def product_detail(product_id):
    product = ProductModel.query.get(product_id)
    return render_template('products/details.html', product=product)


@main.post('/cart-resume/add-product/<int:product_id>/<string:action>')
def action_product_to_cart(product_id, action):
    # if the product already exists only add more quantity of it
    product_size = request.form.get('slc-size')

    if session.get('cart', False) and len([product for product in session['cart'] if product['id'] == product_id and product['size'] == product_size]) > 0:
        cart_product = [
            product for product in session['cart'] if product['id'] == product_id and product['size'] is product_size][0]
        products_filtered = [
            product for product in session.get('cart', []) if product['id'] != product_id or product['size'] != product_size]

        print(f"cart productd {cart_product}")
        print(f"product filtered {products_filtered}")
        print(f"products in sesion {session.get('cart', [])}")
        print(f"product size {product_size}")

        if action == 'add':
            cart_product['quantity'] = cart_product['quantity'] + 1
            products_filtered.append(cart_product)
        else:
            if cart_product['quantity'] > 1:
                cart_product['quantity'] = cart_product['quantity'] - 1
                products_filtered.append(cart_product)

        session['cart'] = products_filtered
    else:
        # search in database and add to the cart
        product = ProductModel.query.get(product_id).to_dict(product_size)
        session['cart'] = [*session['cart'],
                           product] if session.get('cart', False) else [product]

    return redirect(url_for('main.cart_resume'))


@main.get('/cart-resume/remove-product/<int:product_id>')
def remove_product_from_cart(product_id):
    session['cart'] = [product for product in session['cart']
                       if product['id'] != product_id]
    return redirect(url_for('main.cart_resume'))


@main.get('/cart-resume')
def cart_resume():

    if not 'cart' in session or len(session['cart']) < 1:
        return redirect(url_for('main.index'))

    cart_products = [{**product, 'product': ProductModel.query.get(
        product['id']).columns_to_dict()} for product in session['cart']]

    subtotal = 0
    delivery_cost = 99.0
    for item in cart_products:
        subtotal += item['product']['price'] * item['quantity']

    return render_template('cart/resume.html', cart_products=cart_products, subtotal=subtotal, delivery_cost=delivery_cost)


@main.post('/cart-resume')
def create_sale_order():
    items = [{**product, 'product': ProductModel.query.get(
        product['id']).columns_to_dict()} for product in session['cart']]

    total = 99  # costo del envio

    for item in items:
        total += item['product']['price'] * item['quantity']

    # TODO: change the client_id with the current_user.id
    sale_order = SaleOrder(
        reference_number=f"{uuid.uuid4()}"[2:10],
        total=total,
        client_id=1,
        sale_orders_status_id=1,
        created_at=date.today()
    )

    sale_order_details = [SaleOrdeDetail(
        quantity=item['quantity'],
        price=item['product']['price'],
        product_id=item['id'],
        sale_orders=sale_order,
        product_size=item['size']
    ) for item in items]

    db.session.add(sale_order)
    db.session.add_all(sale_order_details)

    db.session.commit()

    preference_data = get_preference_body([*items, {
        "quantity": 1,
        "product": {
            "name": "Envio",
            "price": 99,
        }
    }])

    preference_response = sdk.preference().create(preference_data)
    preference_url = preference_response["response"]["init_point"]

    session['cart'] = []

    return redirect(preference_url)


@main.route('/profile')
@login_required
@roles_accepted('admin', 'client')
def profile():
    return render_template('profile.html', name=current_user.email)


@main.route('/my_orders')
@login_required
# @roles_accepted('admin', 'client')
def my_orders():
    sale_orders = SaleOrder.query.filter_by(client_id=current_user.id).all()
    return render_template('client/my_orders.html', sale_orders=sale_orders)


@main.route('/information')
@login_required
@roles_accepted('admin', 'client')
def information():
    return render_template('information.html')


@main.route('/payment/success')
def success_screen():
    return render_template('status/payment/success.html')


@main.route('/payment/failure')
def failure_screen():
    return render_template('status/payment/failure.html')
