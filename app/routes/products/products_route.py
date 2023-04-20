from flask import Blueprint, render_template, request, redirect, url_for
from ...models.product import Product
from ...controllers.products_controller import getProducts, getProductById, insertProduct, updateProduct, deleteProduct
from flask_security import login_required
from flask_security.decorators import roles_required

products = Blueprint('products', __name__, url_prefix='/admin/products')


@products.route('/products-index')
@login_required
@roles_required('admin')
def index():
    products = getProducts(1)
    return render_template('/admin/products/index_product.html', products=products)


@products.route('/products-insert', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def insert():
    if (request.method == 'POST'):
        name = request.form.get('txtName')
        description = request.form.get('txtDescription')
        price = request.form.get('txtPrice')
        size = request.form.get('cmbSize')
        min_value = request.form.get('txtMinValue')
        max_value = request.form.get('txtMaxValue')
        quantity = request.form.get('txtQuantity')
        filename = request.files['photo']
        product = Product(0, '', name, description, price,
                          size, min_value, max_value, quantity, filename.filename)
        insertProduct(product)
        print('inserting product')

        return redirect(url_for('products.index'))

    return render_template('/admin/products/insert_product.html')


@products.route('/products-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProductById(id)
        return render_template('/admin/products/update_product.html', form=response)

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
        filename = request.files['photo']
        product = Product(id, sku, name, description, price,
                          size, min_value, max_value, quantity, filename)
        updateProduct(product)
        return redirect(url_for('products.index'))


@products.route('/products-delete', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        response = getProductById(id)
        return render_template('/admin/products/delete_product.html', form=response)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteProduct(id)
        return redirect(url_for('products.index'))
