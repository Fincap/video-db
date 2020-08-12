from db import DatabaseController
from videos import generate_videos_list


class Manager:
    """
    This class exists to enforce a consistent model between the database file and the Video object that exist in memory
    """

    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.video_objects = generate_videos_list(self.db_controller)
