import logging
import sqlite3

from db import DatabaseController
from videofunc import generate_videos_list, generate_video

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    conn = sqlite3.connect("data/tables.db")
    database_controller = DatabaseController(conn)
    print("Tables:", database_controller.get_table_names())

    print("Videos:")
    for video in generate_videos_list(database_controller):
        print(video)

    running = True
    while running:
        command = input("Enter your command:\n >").split()

        if command[0] == "add":
            if command[1] == "video":
                try:
                    database_controller.add_new_video(command[2], command[3], command[4])
                except:
                    print("Unable to execute command. Check your arguments.")
            if command[1] == "tag":
                try:
                    database_controller.add_tag(command[2], command[3])
                except:
                    print("Unable to execute command. Check your arguments.")

        if command[0] == "get":
            if command[1] == "video":
                try:
                    video = generate_video(database_controller, command[2])
                    print(video)
                except:
                    print("Unable to execute command. Check your arguments.")
            if command[1] == "tags":
                try:
                    tags = database_controller.get_tags(command[2])
                    print(tags)
                except:
                    print("Unable to execute command. Check your arguments.")

        if command[0] == "exit":
            running = False

    conn.close()
