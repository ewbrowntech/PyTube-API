from fastapi import HTTPException, Query
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
    return v
