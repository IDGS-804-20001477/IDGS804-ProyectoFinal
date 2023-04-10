from ..database.config_db import get_connection


def getBuyOrders():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getBuyOrders()')
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getBuyOrderById(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getBuyOrder(%s)', (id))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def insertBuyOrder(BuyOrder):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            connection.execute('CALL insertBuyOrder(%s, %s, %s, %s, %s)', (
                BuyOrder.total, BuyOrder.provider_id, BuyOrder.quantity, BuyOrder.price, BuyOrder.feedstock_id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateBuyOrder(BuyOrder):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateBuyOrder(%s, %s, %s, %s, %s)', (
                BuyOrder.total, BuyOrder.provider_id, BuyOrder.quantity, BuyOrder.price, BuyOrder.feedstock_id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
    
def deleteBuyOrder(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteBuyOrder(%s)', (id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
