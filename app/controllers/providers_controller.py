from ..database.config_db import get_connection


def getProviders(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProviders(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getProvider(id, create_form):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getProvider(%s)', (id))
            result_set = cursor.fetchall()
            create_form.id.data = result_set[0][0]
            create_form.business_name.data = result_set[0][1]
            create_form.contact_name.data = result_set[0][2]
            create_form.contact_email.data = result_set[0][3]
            create_form.contact_phone.data = result_set[0][4]
            create_form.address.data = result_set[0][5]
            return create_form
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