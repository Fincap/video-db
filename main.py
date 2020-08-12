import logging
import sqlite3

from db import DatabaseController
from objects import get_videos_list

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    conn = sqlite3.connect(":memory:")
    database_controller = DatabaseController(conn)
    print("Tables:", database_controller.get_table_names())

    database_controller.add_new_video(1, "youtube.com/hj34Hd8", "Funny cat video!!")
    database_controller.add_tag(1, "animal")
    database_controller.add_tag(1, "comedy")
    database_controller.add_tag(1, "cat")

    database_controller.add_new_video(2, "youtube.com/h4Hd8jk", "Funny dog video :0")
    database_controller.add_tag(2, "animal")
    database_controller.add_tag(2, "comedy")
    database_controller.add_tag(2, "dog")

    database_controller.add_new_video(3, "youtube.com/ky9rjDF", "sad turtle video :(")
    database_controller.add_tag(3, "animal")
    database_controller.add_tag(3, "drama")
    database_controller.add_tag(3, "turtle")

    for video in get_videos_list(database_controller):
        print(video)

    conn.close()
