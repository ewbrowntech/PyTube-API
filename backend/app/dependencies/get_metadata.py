"""
get_metadata.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Get the available metadata of a YouTube video

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""


async def get_metadata(video):
    """
    Get the available metadata of a YouTube video
    """
    metadata = {
        "id": video.video_id,
        "title": video.title,
        "author": video.author,
        "views": video.views,
        "rating": video.rating,
        "age_restricted": video.age_restricted,
        "publish_date": video.publish_date,
    }
    return metadata
