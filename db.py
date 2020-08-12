import logging
from sqlite3 import Connection

import tabledef


class DatabaseController:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.validate_tables()

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

    # ADD DATA #
    def add_new_video(self, video_id: int, url: str, title: str) -> None:
        with self.connection:
            self.connection.execute("INSERT INTO videos VALUES (?, ?, ?)", (video_id, url, title))

    def add_tag(self, video_id: int, tag_text: str) -> None:
        with self.connection:
            self.connection.execute("INSTERT INTO tags VALUES (?, ?)", (video_id, tag_text))

    # RETRIEVE DATA #
    def get_table_names(self) -> list:
        results = []
        with self.connection:
            for row in self.connection.execute("SELECT name FROM sqlite_master WHERE type='table';"):
                results.append(row)

        return results

    def get_videos(self) -> list:
        results = []
        with self.connection:
            for row in self.connection.execute("SELECT * FROM videos"):
                results.append(row)

        return results

    def get_tags(self, video_id: int) -> list:
        results = []
        with self.connection:
            for row in self.connection.execute("SELECT * FROM tags WHERE video_id = ?", video_id):
                results.append(row)

        return results