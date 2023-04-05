from flask import Blueprint, render_template, request, redirect, url_for
from ...models.product import Product
from ...controllers.products_controller import getProducts, getProductById, insertProduct, updateProduct, deleteProduct

products = Blueprint('products', __name__, url_prefix='/products')


@products.route('/products-index')
def index():
    products = getProducts(1)
    return render_template('/products/index_product.html', products=products)


@products.route('/products-insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        name = request.form.get('txtName')
        description = request.form.get('txtDescription')
        price = request.form.get('txtPrice')
        size = request.form.get('cmbSize')
        min_value = request.form.get('txtMinValue')
        max_value = request.form.get('txtMaxValue')
        quantity = request.form.get('txtQuantity')
        product = Product(0, '', name, description, price,
                          size, min_value, max_value, quantity)
        insertProduct(product)
        return redirect(url_for('products.index'))

    return render_template('/products/insert_product.html')


@products.route('/products-update', methods=['GET', 'POST'])
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProductById(id)
        return render_template('/products/update_product.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        sku = request.form.get('txtSku')
        name = request.form.get('txtName')
        description = request.form.get('txtDescription')
        price = request.form.get('txtPrice')
        size = request.form.get('cmbSize')
        min_value = request.form.get('txtMinValue')
        max_value = request.form.get('txtMaxValue')
        quantity = request.form.get('txtQuantity')
        product = Product(id, sku, name, description, price,
                          size, min_value, max_value, quantity)
        updateProduct(product)
        return redirect(url_for('products.index'))


@products.route('/products-delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProductById(id)
        return render_template('/products/delete_product.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteProduct(id)
        return redirect(url_for('products.index'))
