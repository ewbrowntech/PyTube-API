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
from app.dependencies.get_video import get_video


router = APIRouter()


async def remove_file(filepath: str):
    os.remove(filepath)


@router.get("/", status_code=200)
async def get_video(v: str):
    """
    Get metadata of YouTube video
    """
    return {"v": v}
