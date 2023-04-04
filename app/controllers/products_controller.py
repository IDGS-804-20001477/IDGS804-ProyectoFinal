from ..database.config_db import get_connection


def getProducts(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProducts(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getProductById(id, create_form):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProduct(%s)', (id))
            result_set = cursor.fetchall()
            create_form.id.data = result_set[0][0]
            create_form.sku.data = result_set[0][1]
            create_form.name.data = result_set[0][2]
            create_form.price.data = result_set[0][3]
            create_form.size.data = result_set[0][4]
            create_form.quantity.data = result_set[0][5]
            create_form.min_value.data = result_set[0][6]
            create_form.max_value.data = result_set[0][7]
            create_form.description.data = result_set[0][8]
            return create_form
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
