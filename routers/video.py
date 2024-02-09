"""
routers/videos.py

@Author: Ethan Brown - ethan@ewbrowntech.com

All endpoints for videos/

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from fastapi import APIRouter, Depends, HTTPException
from limiter import limiter
from get_video import get_video

router = APIRouter()


@router.get("/", status_code=200)
async def get_video(v: str = Depends(get_video)):
    """
    Get metadata of YouTube video
    """
    return {"v": v}
