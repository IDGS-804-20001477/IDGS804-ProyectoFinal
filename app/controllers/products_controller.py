from ..database.config_db import get_connection


def getProducts(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProducts(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getProductById(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProduct(%s)', (id))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def insertProduct(Product):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertProduct(%s, %s, %s, %s, %s, %s, %s)', (Product.name, Product.description,
                           Product.price, Product.size, Product.min_value, Product.max_value, Product.quantity))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateProduct(Product):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateProduct(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (Product.id, Product.sku, Product.name,
                           Product.description, Product.price, Product.size, Product.min_value, Product.max_value,
                           Product.quantity))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def deleteProduct(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteProduct(%s)', (id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
