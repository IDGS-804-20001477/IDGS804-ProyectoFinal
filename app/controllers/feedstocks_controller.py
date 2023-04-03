from ..database.config_db import get_connection


def getFeedstocks(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getFeedstocks(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getFeedstockById(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getFeedstock(%s)', (id))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def insertFeedstock(Feedstock):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertFeedstock(%s, %s, %s, %s, %s, %s, %s, %s)', (Feedstock.name, Feedstock.description, Feedstock.price,
                           Feedstock.min_value, Feedstock.max_value, Feedstock.measurement_unit_id, Feedstock.provider_id, Feedstock.quantity))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateFeedstock(Feedstock):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateFeedstock(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (Feedstock.id, Feedstock.name, Feedstock.description,
                           Feedstock.price, Feedstock.min_value, Feedstock.max_value, Feedstock.measurement_unit_id, Feedstock.provider_id, Feedstock.quantity))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def deleteFeedstock(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteFeedstock(%s)', (id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex

def deleteFeedstock(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteFeedstock(%s)', (id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex