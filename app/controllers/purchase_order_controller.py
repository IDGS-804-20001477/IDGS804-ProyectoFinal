from ..database.config_db import get_connection


def getPurchaseOrders():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getPurchaseOrders()')
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getPurchaseOrderById(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getBuyOrder(%s)', (id))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def insertPurchaseOrder(PurchaseOrder):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertBuyOrder(%s, %s, %s)', (PurchaseOrder.total,
                           PurchaseOrder.provider_id, PurchaseOrder.purchase_order_details))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updatePurchaseOrder(id, status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateBuyOrder(%s, %s)', (id, status))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
