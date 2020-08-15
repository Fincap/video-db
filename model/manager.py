from model.db import DatabaseController
from model.videos import generate_videos_list, Video


class Manager:
    """
    This class exists to enforce a consistent model between the database file and the Video object that exist in memory
    """

    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.video_objects = generate_videos_list(self.db_controller)

    def get_new_id(self) -> int:
        used_ids = set(self.video_objects.keys())
        universe = set(range(len(used_ids) + 2))
        return min(universe - used_ids)

    def get_video(self, video_id: int) -> Video:
        return self.video_objects[video_id]

    def get_all_videos(self) -> list:
        videos = []
        for video_id, video in self.video_objects.items():
            videos.append(video)

        return videos

    def add_video(self, url: str, title: str, tags: list = []) -> None:
        new_video_id = self.get_new_id()
        new_video = Video(new_video_id, url, title, tags)

        self.db_controller.add_new_video(new_video_id, url, title)
        self.video_objects[new_video_id] = new_video

        for tag_text in tags:
            self.add_tags(new_video_id, tag_text)

    def add_tags(self, video_id: int, tags: list) -> None:
        for tag in tags:
            if tag not in self.video_objects[video_id].tags:
                self.db_controller.add_tag(video_id, tag)
                self.video_objects[video_id].add_tag(tag)

    def update_video(self):
        pass

    def delete_video(self, video_id: int) -> None:
        if video_id in self.video_objects.keys():
            self.db_controller.delete_video_by_id(video_id)
            del self.video_objects[video_id]

    def delete_tag(self, video_id: int, tag_text: str) -> None:
        self.db_controller.delete_tag(video_id, tag_text)
        self.video_objects[video_id].remove_tag(tag_text)
