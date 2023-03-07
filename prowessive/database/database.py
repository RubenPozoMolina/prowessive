import os
import psycopg2

FIRST_ITEM = 0

query_table_exists = """
SELECT EXISTS (
    SELECT FROM 
        pg_tables
    WHERE 
        schemaname = 'public' AND 
        tablename  = %s
    );
"""

create_files_table = """
CREATE TABLE files (path text, file_bytes bytea);
"""


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
            self.create_table_files()
        except Exception as e:
            print("Error connecting to database:", str(e))

    def query(self, sql, variables=None):
        cursor = self.connection.cursor()
        cursor.execute(sql, variables)
        return_value = cursor.fetchall()
        cursor.close()
        return return_value

    def execute(self, sql, variables=None):
        self.default_cursor.execute(sql, variables)

    def insert_file(self, uri_path, path_to_file):
        try:
            binary_file = open(path_to_file, 'rb').read()
            self.execute(
                "INSERT INTO files (path, file_bytes) VALUES (%s, %s)",
                (uri_path, psycopg2.Binary(binary_file))
            )
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_table_files(self):
        query_result = self.query(query_table_exists, ('files',))
        table_files_exists = query_result[FIRST_ITEM][FIRST_ITEM]
        if not table_files_exists:
            self.execute(create_files_table)

    def delete_file(self, uri_path, path_to_dir):
        try:
            self.execute("SELECT file_bytes FROM files WHERE path = %s", uri_path)
            blob = self.default_cursor.fetchone()
            open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close_connection(self):
        if self.connection:
            self.connection.close()
