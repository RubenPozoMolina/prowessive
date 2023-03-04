import os

import psycopg2


class Database:
    host = None
    port = None
    database = None
    user = None
    password = None
    connection = None
    default_cursor = None

    def __init__(self):
        self.host = os.getenv('DB_HOST', '')
        self.port = os.getenv('DB_PORT', '')
        self.database = os.getenv('DB_NAME', '')
        self.user = os.getenv('DB_USER', '')
        self.password = os.getenv('DB_PASSWORD', '')
        self.connect()

    def __del__(self):
        self.close_connection()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                f"dbname={self.database} user={self.user} password={self.password} host={self.host} port={self.port}"
            )
            self.default_cursor = self.connection.cursor()
        except Exception as e:
            print("Error connecting to database:", str(e))

    def close_connection(self):
        if self.connection:
            self.connection.close()
