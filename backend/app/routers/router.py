"""
routers/videos.py

@Author: Ethan Brown - ethan@ewbrowntech.com

All endpoints for videos/

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import logging
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from app.limiter import limiter
from app.schema import Query
from app.dependencies.perform_search import perform_search
from app.dependencies.get_video import get_video
from app.dependencies.get_metadata import get_metadata
from app.dependencies.get_streams import get_streams
from app.dependencies.get_resolutions import get_resolutions
from app.dependencies.download_audio_stream import download_audio_stream
from app.dependencies.download_video_stream import download_video_stream


router = APIRouter()
logger = logging.getLogger(__name__)


async def remove_file(filepath: str):
    os.remove(filepath)


@router.get("/healthcheck")
async def healthcheck():
    """
    Check the health of the API
    """
    return {"status": "ok"}


@router.get("/search")
async def search(query: Query):
    """
    Perform a YouTube search
    """
    results = await perform_search(query)
    return {"videos": results}


@router.get("/metadata", status_code=200)
async def metadata(v: str):
    """
    Get the available metadata of a YouTube video
    """
    video = await get_video(v)
    metadata = await get_metadata(video)
    streams = await get_streams(video)
    resolutions = await get_resolutions(streams)
    metadata["resolutions"] = resolutions
    return metadata


@router.get("/download/audio", status_code=200)
async def download_audio(
    background_tasks: BackgroundTasks,
    v: str,
):
    """
    Download the audio track of a YouTube video
    """
    # Get the available streams
    video = await get_video(v)
    streams = await get_streams(video)

    # Download the audio stream
    file_info = await download_audio_stream(streams)
    filename = file_info["file_id"] + "." + file_info["extension"]

    # Return the downloaded file
    filepath = os.path.join("/storage", filename)
    background_tasks.add_task(remove_file, filepath)
    return FileResponse(path=filepath, filename=filename)


@router.get("/download/video", status_code=200)
async def video(
    background_tasks: BackgroundTasks,
    v: str,
    resolution: str,
):
    """
    Download the audio track of a YouTube video
    """
    # Get the available streams
    video = await get_video(v)
    streams = await get_streams(video)

    # Download the video stream
    file_info = await download_video_stream(streams, resolution)
    filename = file_info["file_id"] + "." + file_info["extension"]

    # Return the downloaded file
    filepath = os.path.join("/storage", filename)
    background_tasks.add_task(remove_file, filepath)
    return FileResponse(path=filepath, filename=filename)
