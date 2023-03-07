from prowessive.database.database import Database


class TestDatabase:
    def test_connection(self, configuration):
        database = Database()
        assert database.connection

    def test_get_version(self, configuration):
        database = Database()
        version = database.connection.server_version
        assert version == 140001
