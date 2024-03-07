"""
routers/videos.py

@Author: Ethan Brown - ethan@ewbrowntech.com

All endpoints for videos/

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from app.limiter import limiter
from app.get_storage_directory import get_storage_directory
from app.get_video import get_video
from app.main import download_youtube_video


router = APIRouter()


async def remove_file(filepath: str):
    os.remove(filepath)


@router.get("/", status_code=200)
async def get_video(v: str):
    """
    Get metadata of YouTube video
    """
    return {"v": v}


@router.get("/download", status_code=200)
async def download_video(
    background_tasks: BackgroundTasks,
    v: str,
    resolution: str = "480p",
    audio_only: bool = False,
    video_only: bool = False,
):
    """
    Download a YouTube video
    """
    filename = await download_youtube_video(v, resolution, audio_only, video_only)
    filepath = os.path.join(get_storage_directory(), filename)
    background_tasks.add_task(remove_file, filepath)
    return FileResponse(path=filepath, filename=filename)
