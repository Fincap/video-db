# Videos table definition
TABLE_VIDEOS = """
CREATE TABLE videos (
video_id integer PRIMARY KEY,
url text NOT NULL,
title text NOT NULL)
"""

# Tags table definition
TABLE_TAGS = """
CREATE TABLE tags (
video_id integer PRIMARY KEY,
tag_text text NOT NULL,
FOREIGN KEY (video_id)
    REFERENCES videos (video_id) )
"""
