from fastapi import HTTPException, Query


async def get_video(v: str = Query(None, description="YouTube video ID")):
    """
    Get a YouTube video object via PyTube
    """
    if v is None:
        raise HTTPException(
            status_code=400, detail="Query paramater 'v' for video ID is required"
        )
    return v
