import logging
import sqlite3

from db import DatabaseController
from objects import get_videos_list

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    conn = sqlite3.connect("data/tables.db")
    database_controller = DatabaseController(conn)
    print("Tables:", database_controller.get_table_names())

    print("Videos:")
    for video in get_videos_list(database_controller):
        print(video)

    conn.close()
