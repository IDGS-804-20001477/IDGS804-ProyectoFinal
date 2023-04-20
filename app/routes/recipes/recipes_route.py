from flask import Blueprint, request, redirect, url_for, render_template
from ...models.recipe import Recipe
from ...controllers.recipes_controller import getRecipes, getRecipeById, insertRecipe, updateRecipe, deleteRecipe, refillProductByRecipe
from ...controllers.products_controller import getProductsForRecipe
from ...controllers.feedstocks_controller import getFeedstocksForRecipe
from flask_security import login_required
from flask_security.decorators import roles_required
from ...models.product import ProductSize, ProductDetail
from ...models.db import db

recipes = Blueprint('recipes', __name__, url_prefix='/admin/recipes')


@recipes.route('/recipes-index')
@login_required
@roles_required('admin')
def index():
    recipes = getRecipes(1)
    return render_template('/admin/recipes/index_recipe.html', recipes=recipes)


@recipes.route('/recipes-insert', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def insert():

    if (request.method == 'POST'):
        data = request.get_json()
        product_id = int(data['product_id'])
        description = data['description']
        product_size_id = data['product_size_id']
        details = data['array']
        recipe = Recipe(0, product_id, description, details, product_size_id)
        insertRecipe(recipe)
        product_detail = ProductDetail(quantity=0, product_id=product_id,
                                       product_size_id=product_size_id)
        db.session.add(product_detail)
        db.session.commit()
        return redirect(url_for('recipes.index'))

    products = getProductsForRecipe()
    feedstocks = getFeedstocksForRecipe()
    product_sizes = ProductSize.query.all()

    return render_template('/admin/recipes/insert_recipe.html', products=products, feedstocks=feedstocks, product_sizes=product_sizes)


@recipes.route('/recipes-update', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        recipe = getRecipeById(id)
        products = getProductsForRecipe()
        feedstocks = getFeedstocksForRecipe()
        return render_template('/admin/recipes/update_recipe.html', recipe=recipe, products=products, feedstocks=feedstocks)

    if (request.method == 'POST'):
        data = request.get_json()
        id = int(data['id'])
        product_id = int(data['product_id'])
        description = data['description']
        details = data['array']
        recipe = Recipe(id, product_id, description, details)
        print(updateRecipe(recipe))
        return redirect(url_for('recipes.index'))


@recipes.route('/recipes-delete', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        recipe = getRecipeById(id)
        return render_template('/admin/recipes/delete_recipe.html', recipe=recipe)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteRecipe(id)
        return redirect(url_for('recipes.index'))


@recipes.route('/recipes-refill/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def refill(id):
    if (request.method == 'GET'):
        recipe = getRecipeById(id)
        products = getProductsForRecipe()
        feedstocks = getFeedstocksForRecipe()
        return render_template('/admin/recipes/refill_recipe.html', recipe=recipe, products=products, feedstocks=feedstocks)

    if (request.method == 'POST'):
        quantity = request.form['txtQuantity']

        # TODO: check if there are the feedstock enoght for make this recipe
        print(refillProductByRecipe(id, quantity))
        return redirect(url_for('recipes.index'))
