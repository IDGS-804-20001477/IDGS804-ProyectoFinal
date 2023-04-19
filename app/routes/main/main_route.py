from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from flask_security import login_required, current_user
from flask_security.decorators import roles_accepted, roles_required
from ...utils.mercado_pago import sdk

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


# TODO: only for development
products = [
    {
        'sku': 'SK-8923',
        'name': 'VESTIDO TESTING',
        'price': 1000.00,
        'quantity': 1,
        'image': 'https://th.bing.com/th/id/R.5cb3e064c91b65f43d40c69408ac0d9b?rik=keJx1ModJQQmuA&riu=http%3a%2f%2fi.blogs.es%2fec7942%2ftf121c01i-g00-1.1%2f650_1200.jpg&ehk=TMG3nE07hU%2bdZ6AIFnOe7CzPurX4g3T%2bPeW7IWGxP5Y%3d&risl=&pid=ImgRaw&r=0',
        'size': 'M',
    },
    {
        'sku': 'SK-0234',
        'name': 'VESTIDO NEGRO',
        'price': 1500.00,
        'quantity': 1,
        'image': 'https://res.cloudinary.com/walmart-labs/image/upload/w_960,dpr_auto,f_auto,q_auto:best/mg/gm/3pp/asr/07524bb9-5f76-4d87-986f-308dcc9a8134.428b7fe5a123120acbf6aac0ee00ef92.jpeg?odnHeight=2000&odnWidth=2000&odnBg=ffffff',
        'size': 'M',
    }
]

# TODO: only for development


@main.get('/cart-resume/testing')
def testing_method():
    session['cart'] = products
    return redirect(url_for('main.index'))

# TODO: change to post


@main.post('/cart-resume/add-product/<string:product_sku>')
def add_product_to_cart(product_sku):
    if len([product for product in products if product['sku'] == product_sku]) > 0:
        cart_product = [
            product for product in products if product['sku'] == product_sku][0]
        cart_product['quantity'] = cart_product['quantity'] + 1
        session['cart'] = [
            product for product in products if product['sku'] != product_sku]
    else:
        # TODO: search in database and add to the cart
        pass

    session['cart'] = [cart_product] if not 'cart' in session or len(session['cart']) < 1 else [
        *session['cart'], cart_product]
    return redirect(url_for('main.cart_resume'))


@main.get('/cart-resume/remove-product/<string:product_sku>')
def remove_product_from_cart(product_sku):
    print(product_sku)
    session['cart'] = [product for product in session['cart']
                       if product['sku'] != product_sku]
    return redirect(url_for('main.cart_resume'))


@main.get('/cart-resume')
def cart_resume():

    if not 'cart' in session or len(session['cart']) < 1:
        return redirect(url_for('main.index'))

    cart_products = session['cart']
    return render_template('cart/resume.html', cart_products=cart_products)


@main.post('/cart-resume')
def create_preference():
    preference_data = {
        "items": [
            {
                "title": "Vestido Negro",
                "quantity": 1,
                "unit_price": 700.00,
                "currency_id": "MXN",
                "picture_url": "https://res.cloudinary.com/walmart-labs/image/upload/w_960,dpr_auto,f_auto,q_auto:best/mg/gm/3pp/asr/07524bb9-5f76-4d87-986f-308dcc9a8134.428b7fe5a123120acbf6aac0ee00ef92.jpeg?odnHeight=2000&odnWidth=2000&odnBg=ffffff",
                "description": "Descripción del VESTIDO NEGRO",
            }
        ],
        "payer": {
            "name": "Juan",
            "surname": "Lopez",
            "email": "user@email.com",
            "phone": {
                "area_code": "11",
                "number": "4444-4444"
            },
            "identification": {
                "type": "DNI",
                "number": "12345678"
            },
            "address": {
                "street_name": "Street",
                "street_number": 123,
                "zip_code": "5700"
            }
        },
        "back_urls": {
            "success": "https://www.success.com",
            "failure": "http://www.failure.com",
            "pending": "http://www.pending.com"
        },
        "notification_url": "https://www.your-site.com/ipn",
        "statement_descriptor": "MINEGOCIO",
        "external_reference": "Reference_1234",
    }

    preference_response = sdk.preference().create(preference_data)
    preference_url = preference_response["response"]["init_point"]
    return redirect(preference_url)


@main.route('/payment/success')
def success_screen():
    return render_template('status/payment/success.html')

@main.route('/payment/failure')
def failure_screen():
    return render_template('status/payment/failure.html')

@main.route('/profile')
@login_required
@roles_accepted('admin', 'client')
def profile():
    return render_template('profile.html', name=current_user.email)


@main.route('/information')
@login_required
@roles_accepted('admin', 'client')
def information():
    return render_template('information.html')
