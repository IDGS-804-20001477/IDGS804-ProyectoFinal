from flask import Blueprint, render_template, request, redirect, url_for
from ...models.forms import ProductForm
from ...models.product import Product
from ...controllers.products_controller import getProducts, getProductById, insertProduct, updateProduct, deleteProduct

products = Blueprint('products', __name__)


@products.route('/products-index')
def index():
    create_form = ProductForm(request.form)
    products = getProducts(1)
    return render_template('index_product.html', products=products, form=create_form)


@products.route('/products-insert', methods=['GET', 'POST'])
def insert():
    create_form = ProductForm(request.form)

    if (request.method == 'POST'):
        product = Product(0, '', create_form.name.data, create_form.description.data, create_form.price.data,
                          create_form.size.data, create_form.min_value.data, create_form.max_value.data, create_form.quantity.data)
        insertProduct(product)
        return redirect(url_for('products.index'))

    return render_template('insert_product.html', form=create_form)


@products.route('/products-update', methods=['GET', 'POST'])
def update():
    create_form = ProductForm(request.form)

    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProductById(id, create_form)
        return render_template('update_product.html', form=response)

    if (request.method == 'POST'):
        product = Product(create_form.id.data, create_form.sku.data, create_form.name.data, create_form.description.data,
                          create_form.price.data, create_form.size.data, create_form.min_value.data, create_form.max_value.data,
                          create_form.quantity.data)
        updateProduct(product)
        return redirect(url_for('products.index'))


@products.route('/products-delete', methods=['GET', 'POST'])
def delete():
    create_form = ProductForm(request.form)

    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProductById(id, create_form)
        return render_template('delete_product.html', form=response)

    if (request.method == 'POST'):
        deleteProduct(create_form.id.data)
        return redirect(url_for('products.index'))
