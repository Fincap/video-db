from PyQt5 import QtWidgets

from db import DatabaseController


class Video(QtWidgets.QListWidgetItem):

    def __init__(self, video_id: int, url: str, title: str, tags: list = []) -> None:
        super().__init__(title)
        self.video_id = video_id
        self.url = url
        self.title = title
        self.tags = tags

    def __str__(self) -> str:
        return "%s: %s (%s), %s" % (self.video_id, self.title, self.url, self.tags)

    def add_tag(self, tag_text: str) -> None:
        self.tags.append(tag_text)

    def remove_tag(self, tag_text: str) -> None:
        self.tags.remove(tag_text)


def generate_videos_list(controller: DatabaseController) -> dict:
    videos = {}

    video_tuples = controller.get_videos()
    for video_tuple in video_tuples:
        new_video_id = video_tuple["video_id"]

        videos[new_video_id] = generate_video(controller, new_video_id)

    return videos


def generate_video(controller: DatabaseController, video_id: int) -> Video:
    video_tuple = controller.get_video_by_id(video_id)

    new_video_id = video_tuple["video_id"]
    new_video_url = video_tuple["url"]
    new_video_title = video_tuple["title"]

    tag_tuples = controller.get_tags(video_id)
    new_tags = []
    for tag_tuple in tag_tuples:
        new_tags.append(tag_tuple["tag_text"])

    return Video(new_video_id, new_video_url, new_video_title, new_tags)
