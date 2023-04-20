from ..database.config_db import get_connection


def getRecipes(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getRecipes(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getRecipeById(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getRecipe(%s)', (id))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def insertRecipe(Recipe):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertRecipe(%s, %s, %s)',
                           (Recipe.product_id, Recipe.description, Recipe.recipe_details))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateRecipe(Recipe):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateRecipe(%s, %s, %s, %s)', (Recipe.id,
                           Recipe.product_id, Recipe.description, Recipe.recipe_details))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def deleteRecipe(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteRecipe(%s)', id)
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def refillProductByRecipe(id, quantity):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL refillProducts(%s, %s)', (id, quantity))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex