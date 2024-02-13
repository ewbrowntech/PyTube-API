"""
download_audio_stream.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Download a YouTube audio stream to a given path

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import secrets
from pytube.query import StreamQuery
from get_storage_directory import get_storage_directory


async def download_audio_stream(streams: StreamQuery):
    # Get the audio stream with the highest audio bitrate
    audio_streams = streams.filter(only_audio=True)
    preferred_stream = audio_streams.order_by("abr").last()

    # Download the audio stream
    file_id = secrets.token_hex(4)
    filename = file_id + ".mp3"
    preferred_stream.download(get_storage_directory(), filename)

    return file_id
