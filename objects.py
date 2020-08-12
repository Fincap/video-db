from db import DatabaseController


def get_videos_list(controller: DatabaseController) -> list:
    videos = []

    video_tuples = controller.get_videos()
    for video_tuple in video_tuples:
        new_video_id = video_tuple[0]
        new_video_url = video_tuple[1]
        new_video_title = video_tuple[2]

        tag_tuples = controller.get_tags(video_tuple[0])
        new_tags = []
        for tag_tuple in tag_tuples:
            new_tags.append(tag_tuple[2])

        new_video = Video(new_video_id, new_video_url, new_video_title, new_tags)
        videos.append(new_video)

    return videos


class Video:

    def __init__(self, video_id: int, url: str, title: str, tags:list) -> None:
        self.video_id = video_id
        self.url = url
        self.title = title
        self.tags = tags

    def __str__(self) -> str:
        return "%s: %s (%s), %s" % (self.video_id, self.title, self.url, self.tags)
