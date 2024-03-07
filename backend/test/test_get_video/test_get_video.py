"""
test_get_video.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Test functionality of get_video() [GET /videos]

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import pytest
from fastapi import HTTPException
from app.dependencies.get_video import get_video


@pytest.mark.asyncio
async def test_get_video_000_nominal(test_client):
    """
    Test 000 - Nominal
    Conditions: v=dQw4w9WgXcQ
    Result: YouTube object returned
    """
    video = await get_video(v="dQw4w9WgXcQ")
    assert video.title == "Never Gonna Give You Up"


@pytest.mark.asyncio
async def test_get_video_001_anomalous_no_video_id(test_client):
    """
    Test 001 - Anomalous
    Conditions: No video ID is provided in query parameter
    Result: "400: The provided video ID does not meet the required format"
    """
    with pytest.raises(HTTPException) as e:
        video = await get_video(v=None)
    assert str(e.value) == "400: Query paramater 'v' for video ID is required"


@pytest.mark.asyncio
async def test_get_video_002_anomalous_id_too_short(test_client):
    """
    Test 002 - Anomalous
    Conditions: v=dQw4w9WgXc
    Result: HTTP 400 - "The provided video ID does not meet the required format"
    """
    with pytest.raises(HTTPException) as e:
        video = await get_video(v="dQw4w9WgXc")
    assert (
        str(e.value) == "400: The provided video ID does not meet the required format"
    )


@pytest.mark.asyncio
async def test_get_video_003_anomalous_id_too_long(test_client):
    """
    Test 003 - Anomalous
    Conditions: v=dQw4w9WgXcQc
    Result: HTTP 400 - "The provided video ID does not meet the required format"
    """
    with pytest.raises(HTTPException) as e:
        video = await get_video(v="dQw4w9WgXcQcc")
    assert (
        str(e.value) == "400: The provided video ID does not meet the required format"
    )


@pytest.mark.asyncio
async def test_get_video_004_anomalous_id_invalid_characters(test_client):
    """
    Test 004 - Anomalous
    Conditions: v=dQw4w9WgXc!
    Result: HTTP 400 - "The provided video ID does not meet the required format"
    """
    with pytest.raises(HTTPException) as e:
        video = await get_video(v="dQw4w9WgXc!")
    assert (
        str(e.value) == "400: The provided video ID does not meet the required format"
    )
