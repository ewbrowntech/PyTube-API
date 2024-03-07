"""
download_video_stream.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Download a YouTube video stream to a given path

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import logging
import secrets
from pytube.query import StreamQuery
from app.dependencies.get_preferred_stream import get_preferred_stream

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


async def download_video_stream(streams: StreamQuery, resolution: str):
    # Get the video stream with the most compatible codec at the given resolution
    video_streams = streams.filter(only_video=True)
    preferred_stream = await get_preferred_stream(video_streams, resolution)
    logger.info(str(preferred_stream))
    # Download the video stream
    file_id = secrets.token_hex(4)
    file_extension = "." + preferred_stream.mime_type.split("/")[1]
    filename = "video-stream-" + file_id + file_extension
    preferred_stream.download("/storage", filename)

    return file_id, file_extension
