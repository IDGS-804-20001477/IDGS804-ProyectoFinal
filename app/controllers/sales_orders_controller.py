from ..database.config_db import get_connection


def getSalesOrders():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getSaleOrders()')
            return cursor.fetchall()
    except Exception as ex:
        return ex
    
    
def getSaleOrderStatus():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getSaleOrderStatus()')
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getSaleOrderById(id, create_form):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getSaleOrder(%s)', (id))
            result_set = cursor.fetchall()
    except Exception as ex:
        return ex


def insertSaleOrder(SaleOrder):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            connection.execute('CALL insertSaleOrder(%s, %s, %s)', (
                SaleOrder.total, SaleOrder.client_id, SaleOrder.sale_order_details))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateSaleOrder(id, status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateSaleOrder(%s, %s)', (id, status))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
