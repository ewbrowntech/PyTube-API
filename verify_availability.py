"""
verify_availability.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Verify the availability of a video, given either a YouTube object or a URL

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from fastapi import HTTPException
from pytube import YouTube
from exceptions import ArgumentError
from pytube.exceptions import (
    AgeRestrictedError,
    MembersOnly,
    RecordingUnavailable,
    VideoPrivate,
    VideoUnavailable,
    VideoRegionBlocked,
    LiveStreamError,
)
from exceptions import ArgumentError
from get_video import get_video


async def verify_availability(youtube: YouTube = None, v: str = None):
    """
    Verify the availability of a video, given either a YouTube object or a URL

    Args:
        youtube (YouTube, optional): A PyTube YouTube object to be verified. Default is None.
        v (str, optional): A YouTube video ID. Must be a string if provided. Default is None.
    """
    # Validate arguments. Accepts either a YouTube object or a URL string
    if youtube is None and v is None:
        raise ArgumentError("Either argument 'youtube' or 'v' must be provided.")
    if youtube is not None and v is not None:
        raise ArgumentError(
            "Cannot accept both arguments 'youtube' and 'v'. One and only one should be provided."
        )
    if youtube is not None and not isinstance(youtube, YouTube):
        raise TypeError("Argument 'youtube' must be a YouTube object")
    if v is not None and not isinstance(v, str):
        raise TypeError("Argument 'v' must be a string")

    # Get the video object if one was not provided
    if youtube is None and v is not None:
        youtube = await get_video(v)

    # Verify the availability of the YouTube object and raise the correct HTTP Exception if it is not available
    try:
        youtube.check_availability()
    except RecordingUnavailable as e:
        raise HTTPException(status_code=404, detail=str(e))
    except LiveStreamError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except VideoRegionBlocked as e:
        raise HTTPException(status_code=403, detail=str(e))
    except VideoPrivate as e:
        raise HTTPException(status_code=403, detail=str(e))
    except VideoUnavailable as e:
        raise HTTPException(status_code=404, detail=str(e))

    return True
