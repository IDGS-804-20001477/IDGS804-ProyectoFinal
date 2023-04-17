from ..database.config_db import get_connection


def getUsers(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getUsers(%s)', (status))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getUserById(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getUser(%s)', (id))
            return cursor.fetchall()
    except Exception as ex:
        return ex


def getUserTypes(status):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL getUserTypes(%s)', (status))
    except Exception as ex:
        return ex


def insertUser(User):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL insertUser(%s, %s, %s, %s, %s, %s, %s)', (User.email,
                           User.password, User.type, User.name, User.lastname, User.address, User.phone))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateUser(User):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateUser(%s, %s, %s, %s, %s, %s, %s, %s)', (User.id, User.email,
                           User.password, User.type, User.name, User.lastname, User.address, User.phone))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def updateProfile(User):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL updateProfile(%s, %s, %s, %s, %s)',
                           (User.id, User.name, User.lastname, User.address, User.phone))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex


def deleteUser(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL deleteUser(%s)', (id))
        connection.commit()
        connection.close()
    except Exception as ex:
        return ex
