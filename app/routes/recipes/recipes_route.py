from flask import Blueprint, request, redirect, url_for, render_template
from ...models.recipe import Recipe
from ...controllers.recipes_controller import getRecipes, getRecipeById, insertRecipe, updateRecipe, deleteRecipe
from ...controllers.products_controller import getProducts
from ...controllers.feedstocks_controller import getFeedstocks


recipes = Blueprint('recipes', __name__, url_prefix='/admin/recipes')


@recipes.route('/recipes-index')
def index():
    recipes = getRecipes(1)
    return render_template('/admin/recipes/index_recipe.html', recipes=recipes)


@recipes.route('/recipes-insert', methods=['GET', 'POST'])
def insert():
    products = getProducts(1)
    feedstocks = getFeedstocks(1)

    if (request.method == 'POST'):
        product_id = request.form.get('cmbProducts')
        description = request.form.get('txtDescription')
        details = request.form.get('<<agregar un nombre>>')
        recipe = Recipe(0, description, product_id, details)
        insertRecipe(recipe)
        return redirect(url_for('recipes.index'))

    return render_template('/admin/recipes/insert_recipe.html', products=products, feedstocks=feedstocks)


@recipes.route('/recipes-update', methods=['GET', 'POST'])
def update():
    if (request.method == 'GET'):
        id = request.args.get('id')
        recipe = getRecipeById(id)
        products = getProducts(1)
        feedstocks = getFeedstocks(1)
        return render_template('/admin/recipes/update_recipe.html', recipe=recipe, products=products, feedstocks=feedstocks)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        product_id = request.form.get('cmbProducts')
        description = request.form.get('txtDescription')
        details = request.form.get('<<agregar un nombre>>')
        recipe = Recipe(id, description, product_id, details)
        updateRecipe(recipe)
        return redirect(url_for('recipes.index'))


@recipes.route('/recipes-delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'GET'):
        id = request.args.get('id')
        recipe = getRecipeById(id)
        return render_template('/admin/recipes/delete_recipe.html', recipe=recipe)

    if (request.method == 'POST'):
        id = request.form.get('txtId')
        deleteRecipe(id)
        return redirect(url_for('recipes.index'))
