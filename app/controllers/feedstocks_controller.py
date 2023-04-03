from ..database.config_db import get_connection


def getFeedstocks(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getFeedstocks(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getFeedstockById(id, create_form):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getFeedstock(%s)', (id))
            result_set = cursor.fetchall()
            create_form.id.data = result_set[0][0]
            create_form.name.data = result_set[0][1]
            create_form.description.data = result_set[0][2]
            create_form.price.data = result_set[0][3]
            create_form.min_value.data = result_set[0][4]
            create_form.max_value.data = result_set[0][5]
            create_form.quantity.data = result_set[0][6]
            create_form.measurement_unit_id.data = result_set[0][7]
            create_form.provider_id.data = result_set[0][8]
            return create_form
    except Exception as ex:
        return ex


def insertFeedstock(Feedstock):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertFeedstock(%s, %s, %s, %s, %s, %s, %s)', (Feedstock.feedstock_id.name, Feedstock.feedstock_id.description,
                           Feedstock.feedstock_id.price, Feedstock.feedstock_id.min_value, Feedstock.feedstock_id.max_value, Feedstock.feedstock_id.measurement_unit_id, Feedstock.feedstock_id.provider_id, Feedstock.quantity))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateFeedstock(Feedstock):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateFeedstock(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (Feedstock.feedstock_id.name, Feedstock.feedstock_id.description,
                           Feedstock.feedstock_id.price, Feedstock.feedstock_id.min_value, Feedstock.feedstock_id.max_value, Feedstock.feedstock_id.measurement_unit_id, Feedstock.feedstock_id.provider_id, Feedstock.quantity))
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