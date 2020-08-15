import logging
import sqlite3

from db import DatabaseController
from model import Manager
from videos import generate_videos_list, generate_video

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    conn = sqlite3.connect("data/tables.db")
    database_controller = DatabaseController(conn)
    print("Tables:", database_controller.get_table_names())

    print("Videos:")
    for video_id, video in generate_videos_list(database_controller).items():
        print(video)

    manager = Manager(database_controller)

    running = True
    while running:
        print(manager.get_new_id())
        command = input("Enter your command:\n >").split()

        if command[0] == "add":
            if command[1] == "video":
                try:
                    manager.add_video(command[2], command[3])
                except:
                    print("Unable to execute command. Check your arguments.")
            if command[1] == "tag":
                try:
                    manager.add_tag(int(command[2]), command[3])
                except:
                    print("Unable to execute command. Check your arguments.")

        if command[0] == "get":
            if command[1] == "video":
                try:
                    video = manager.get_video(int(command[2]))
                    print(video)
                except:
                    print("Unable to execute command. Check your arguments.")
            if command[1] == "tags":
                try:
                    tags = manager.get_video(int(command[2])).tags
                    print(tags)
                except:
                    print("Unable to execute command. Check your arguments.")

        if command[0] == "delete":
            if command[1] == "video":
                try:
                    database_controller.delete_video_by_id(int(command[2]))
                except:
                    print("Unable to execute command. Check your arguments.")
            if command[1] == "tag":
                try:
                    database_controller.delete_tag(int(command[2]), command[3])
                except:
                    print("Unable to execute command. Check your arguments.")

        if command[0] == "exit":
            running = False

    conn.close()
