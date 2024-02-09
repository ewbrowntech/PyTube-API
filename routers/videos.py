"""
routers/videos.py

@Author: Ethan Brown - ethan@ewbrowntech.com

All endpoints for videos/

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from fastapi import APIRouter, HTTPException
from limiter import limiter


router = APIRouter()


@router.get("/", status_code=200)
async def get_video(v: str = None):
    if v is None:
        return HTTPException(
            status_code=400, detail="Query paramater 'v' for video ID is required"
        )
