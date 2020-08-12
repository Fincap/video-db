from db import DatabaseController


class Video:

    def __init__(self, video_id: int, url: str, title: str, tags:list) -> None:
        self.video_id = video_id
        self.url = url
        self.title = title
        self.tags = tags

    def __str__(self) -> str:
        return "%s: %s (%s), %s" % (self.video_id, self.title, self.url, self.tags)
