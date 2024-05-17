import mysql.connector


class Database:

    host = '0.tcp.jp.ngrok.io'
    user = 'test'
    password = 'Test543!'
    database = 'studydp'

    # change port
    port = 15931

    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

    def query(self, sql):
        self.cursor.execute(sql)

    def get_all(self):
        return self.cursor.fetchall()

    def get_one(self):
        return self.cursor.fetchone()
