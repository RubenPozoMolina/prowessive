from prowessive.database.database import Database


class TestDatabase:
    def test_connection(self, configuration):
        database = Database()
        assert database.connection
