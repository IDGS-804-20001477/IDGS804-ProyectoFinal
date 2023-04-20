from ..database.config_db import get_connection


def getSalesPerMonth(month):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getSalesPerMonth(%s)', (month))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getPurchasesPerMonth(month):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getPurchasesPerMonth(%s)', (month))
            return cursor.fetchall()
    except Exception as ex:
        return ex
    
    
def getLeadingProduct(month):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getLeadingProduct(%s)', (month))
            return cursor.fetchall()
    except Exception as ex:
        return ex