from sqlalchemy import create_engine

from interface.connection_interface import ConnectDB


class ConnectionSQLite(ConnectDB):

    def connection(self):
        engine = create_engine("sqlite+pysqlite:///database.db", echo=True)
        return engine

