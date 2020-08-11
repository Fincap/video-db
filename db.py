import logging
from sqlite3 import Connection

import tabledef


class DatabaseController:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.validate_tables()

    def get_table_names(self) -> list:
        results = self.connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = []
        for name in results:
            tables.append(name[0])

        return tables

    def validate_tables(self) -> None:
        # Check if the tables exist. If not, create them.
        table_names = self.get_table_names()
        if 'videos' not in table_names:
            logging.info("Table not found: videos. Creating table.")
            with self.connection:
                self.connection.execute(tabledef.TABLE_VIDEOS)

        if 'tags' not in table_names:
            logging.info("Table not found: tags. Creating table.")
            with self.connection:
                self.connection.execute(tabledef.TABLE_TAGS)

    def add_new_video(self, video_id: int, url: str, title: str):
        pass
