import  mysql.connector


import mysql.connector

class ConnectorDatabase:

    def __init__(self, host, user, password, database, port):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=int(port)
        )

    def execute_and_fetchone(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    def execute_and_commit(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(e)
            self.connection.rollback()
