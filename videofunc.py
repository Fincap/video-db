from db import DatabaseController
from objects import Video


def generate_videos_list(controller: DatabaseController) -> list:
    videos = []

    video_tuples = controller.get_videos()
    for video_tuple in video_tuples:
        new_video_id = video_tuple[0]

        videos.append(generate_video(controller, new_video_id))

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
