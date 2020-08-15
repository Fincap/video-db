from db import DatabaseController
from videos import generate_videos_list


class Manager:
    """
    This class exists to enforce a consistent model between the database file and the Video object that exist in memory
    """

    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.video_objects = generate_videos_list(self.db_controller)
        self.used_ids = self.get_used_ids()

    def get_used_ids(self) -> set:
        ids = set()
        for video in self.video_objects:
            ids.add(video.video_id)

        return ids

    def get_new_id(self):
        universe = set(range(1, len(self.used_ids) + 2))
        return min(universe - self.used_ids)

    def add_video(self):
        pass

    def add_tag(self):
        pass

    def update_video(self):
        pass

    def delete_video(self):
        pass

    def delete_tag(self):
        pass
