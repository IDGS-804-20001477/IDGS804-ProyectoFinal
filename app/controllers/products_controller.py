from ..database.config_db import get_connection
from flask import request
from PIL import Image
import io
import base64


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
            cursor.execute('CALL insertProduct(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (Product.name, Product.description, Product.price,
                           Product.size, Product.min_value, Product.max_value, Product.photo, convertImageToBase64(), Product.quantity))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateProduct(Product):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateProduct(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (Product.id, Product.sku, Product.name, Product.description,
                           Product.price, Product.size, Product.min_value, Product.max_value, Product.photo, convertImageToBase64(), Product.quantity))
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


def convertImageToBase64():
    file = request.files['photo']
    img = Image.open(file)
    buffered = io.BytesIO()
    img.save(buffered, format='PNG')
    return base64.b64encode(buffered.getvalue()).decode('utf-8')
