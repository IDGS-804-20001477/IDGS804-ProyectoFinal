from flask import Blueprint, request, redirect, url_for, render_template
from ...models.recipe import Recipe
from ...controllers.recipes_controller import getRecipes, getRecipeById, insertRecipe, updateRecipe, deleteRecipe
from ...controllers.products_controller import getProducts


recipes = Blueprint('recipes', __name__)


@recipes.route('/recipes-index')
def index():
    recipes = getRecipes(1)
    products = getProducts(1)
    return render_template('index_recipe.html', recipes=recipes, products=products)


@recipes.route('/recipes-insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        product_id = request.form.get('cmbProducts')
        description = request.form.get('txtDescription')
        details = request.form.get('<<agregar un nombre>>')
        recipe = Recipe(0, description, product_id, details)
        insertRecipe(recipe)
        return redirect(url_for('recipes.index'))

    return render_template('insert_recipe.html')


@recipes.route('/recipes-update', methods=['GET', 'POST'])
def update():
    if(request.method == 'GET'):
        id = request.args.get('id')
        recipe = getRecipeById(id)
        return render_template('update_recipe.html', recipe=recipe)
    
    if(request.method == 'POST'):
        id = request.form.get('txtId')
        product_id = request.form.get('cmbProducts')
        description = request.form.get('txtDescription')
        details = request.form.get('<<agregar un nombre>>')
        recipe = Recipe(id, description, product_id, details)
        updateRecipe(recipe)
        return redirect(url_for('recipes.index'))


@recipes.route('/recipes-delete', methods=['GET', 'POST'])
def delete():
    if(request.method == 'GET'):
        id = request.args.get('id')
        recipe = getRecipeById(id)
        return render_template('delete_recipe.html', recipe=recipe)
    
    if(request.method == 'POST'):
        id = request.form.get('txtId')
        deleteRecipe(id)
        return redirect(url_for('recipes.index'))