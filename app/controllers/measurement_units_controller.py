from ..database.config_db import get_connection


def getMeasurementUnits(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getMeasurementUnits(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex
