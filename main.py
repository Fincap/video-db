import logging
import sqlite3

from db import DatabaseController
from model import Manager

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    conn = sqlite3.connect("data/tables.db")
    database_controller = DatabaseController(conn)
    print("Tables:", database_controller.get_table_names())

    manager = Manager(database_controller)

    running = True
    while running:
        print("\n\n\nUnused ID: ", manager.get_new_id())
        for video_id, video in manager.video_objects.items():
            print(video)

        command = input("\nEnter your command:\n >").split()

        if command[0] == "add":
            if command[1] == "video":
                try:
                    title = ' '.join(command[3:])
                    manager.add_video(command[2], title)
                except:
                    print("Unable to execute command. Check your arguments.")
            if command[1] == "tags":
                manager.add_tags(int(command[2]), command[3:])

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
                manager.delete_video(int(command[2]))
            if command[1] == "tag":
                try:
                    manager.delete_tag(int(command[2]), command[3])
                except:
                    print("Unable to execute command. Check your arguments.")

        if command[0] == "exit":
            running = False

    conn.close()
