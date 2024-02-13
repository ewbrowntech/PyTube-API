"""
get_streams.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Get the available streams of a YouTube video

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from pytube import YouTube
from fastapi import HTTPException
from pytube.exceptions import AgeRestrictedError
from exceptions import ArgumentError


async def get_streams(youtube: YouTube):
    if youtube is None:
        raise ArgumentError("Argument 'youtube' was None")
    if youtube is not None and not isinstance(youtube, YouTube):
        raise TypeError("Argument 'youtube' must be a YouTube object")
    try:
        streams = youtube.streams
    except AgeRestrictedError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return streams
