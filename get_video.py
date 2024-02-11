"""
get_video.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Verify the availability of a video, given either a YouTube object or a URL

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from fastapi import HTTPException, Query
from pytube import YouTube
from pytube.exceptions import (
    AgeRestrictedError,
    MembersOnly,
    RecordingUnavailable,
    VideoPrivate,
    VideoUnavailable,
    VideoRegionBlocked,
    LiveStreamError,
)
import re


async def get_video(v: str = Query(None, description="YouTube video ID")):
    """
    Get a YouTube video object via PyTube
    """
    if v is None:
        raise HTTPException(
            status_code=400, detail="Query paramater 'v' for video ID is required"
        )
    if len(v) != 11:
        raise HTTPException(
            status_code=400,
            detail="The provided video ID does not meet the required format",
        )
    if not re.search(r"([0-9A-Za-z_-]{11})", v):
        raise HTTPException(
            status_code=400,
            detail="The provided video ID does not meet the required format",
        )
    video = YouTube("?v=" + v)
    return video
