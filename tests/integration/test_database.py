import pytest

from prowessive.database.database import Database

create_table = """
CREATE TABLE test_files (file_name text, file_bytes bytea);
"""

drop_table = """
DROP TABLE test_files;
"""

delete_files = """
DELETE FROM files;
"""

query_files = """
SELECT path, file_bytes from files
"""


@pytest.fixture(scope="session", autouse=True)
def database(configuration):
    local_database = Database(create_tables=False)
    local_database.execute(create_table)
    yield local_database
    local_database.execute(drop_table)


class TestDatabase:
    def test_connection(self, database):
        assert database.connection

    def test_get_version(self, database):
        version = database.connection.server_version
        assert version == 140001

    def test_database_file(self, database):
        database.insert_file('/test/index.html', 'tests/files/index.html')
        files = database.query(query_files)
        print(files)
        assert len(files) > 0

    def test_load_files_from_path(self, database):
        database.create_table_files()
        database.execute(delete_files)
        database.load_files_from_path('prowessive/www')
        files = database.query(query_files)
        assert len(files) >= 2
