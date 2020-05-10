import mysql.connector

def connectarBD():

    database = mysql.connector.connect(
        host = 'localhost',
        user = 'admin',
        passwd = 'admin',
        database = 'pi_dockers'
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]