from ..database.config_db import get_connection


def getProviders(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProviders(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getProviderById(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProvider(%s)', (id))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def insertProvider(Provider):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertProvider(%s, %s, %s, %s, %s)', (Provider.business_name,
                           Provider.contact_name, Provider.contact_email, Provider.contact_phone, Provider.address))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateProvider(Provider):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateProvider(%s, %s, %s, %s, %s, %s)', (Provider.id, Provider.business_name,
                           Provider.contact_name, Provider.contact_email, Provider.contact_phone, Provider.address))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def deleteProvider(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteProvider(%s)', (id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
