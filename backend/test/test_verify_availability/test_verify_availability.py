"""
test_verify_availability.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Test the functionality of verify_availability()

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import pytest
from fastapi import HTTPException
from backend.exceptions import ArgumentError
from backend.get_video import get_video
from backend.verify_availability import verify_availability


@pytest.mark.asyncio
async def test_verify_availability_000_nominal_youtube_provided():
    """
    Test 000 - Nominal
    Conditions: Nominal YouTube object provided
    Result: True
    """
    video = await get_video("dQw4w9WgXcQ")
    assert await verify_availability(youtube=video)


@pytest.mark.asyncio
async def test_verify_availability_001_nominal_id_provided():
    """
    Test 001 - Nominal
    Conditions: Nominal video ID provided
    Result: True
    """
    assert await verify_availability(v="dQw4w9WgXcQ")


@pytest.mark.asyncio
async def test_verify_availability_002_anomalous_no_youtube_or_id_provided():
    """
    Test 002 - Anomalous
    Conditions: Neither YouTube object nor ID provided
    Result: ArgumentError - "Either argument 'youtube' or 'v' must be provided."
    """
    with pytest.raises(ArgumentError) as e:
        await verify_availability()
    assert str(e.value) == "Either argument 'youtube' or 'v' must be provided."


@pytest.mark.asyncio
async def test_verify_availability_003_anomaluos_youtube_and_id_provided():
    """
    Test 003 - Anomalous
    Conditions: Both YouTube object and ID provided
    Result: ArgumentError - "Cannot accept both arguments 'youtube' and 'v'. One and only one should be provided.
    """
    video = await get_video("dQw4w9WgXcQ")
    with pytest.raises(ArgumentError) as e:
        await verify_availability(youtube=video, v="dQw4w9WgXcQ")
    assert (
        str(e.value)
        == "Cannot accept both arguments 'youtube' and 'v'. One and only one should be provided."
    )


@pytest.mark.asyncio
async def test_verify_availability_004_anomalous_video_unavailable():
    """
    Test 004 - Anomalous
    Conditions: v=aaaaaaaaaaa
    Result: HTTP 404 - "aaaaaaaaaaa is unavailable"
    """
    with pytest.raises(HTTPException) as e:
        video = await verify_availability(v="aaaaaaaaaaa")
    assert str(e.value) == "404: aaaaaaaaaaa is unavailable"


@pytest.mark.asyncio
async def test_verify_availability_005_anomalous_livestream_recording_unavailable():
    """
    Test 005 - Anomalous
    Conditions: v=5YceQ8YqYMc
    Result: HTTP 404 - "5YceQ8YqYMc does not have a live stream recording available"
    """
    with pytest.raises(HTTPException) as e:
        video = await verify_availability(v="5YceQ8YqYMc")
    assert (
        str(e.value)
        == "404: 5YceQ8YqYMc does not have a live stream recording available"
    )


# @pytest.mark.asyncio
# async def test_verify_availability_006_anomalous_livestream_error():
#     """
#     Test 006 - Anomalous
#     Conditions: v=YLnZklYFe7E | Video is an active livestream
#     Result: HTTP 404 - "YLnZklYFe7E is streaming live and cannot be loaded"
#     """
#     with pytest.raises(HTTPException) as e:
#         video = await verify_availability(v="YLnZklYFe7E")
#     assert str(e.value) == "404: YLnZklYFe7E is streaming live and cannot be loaded"


# @pytest.mark.asyncio
# async def test_verify_availability_007_anomalous_region_lock():
#     """
#     Test 007 - Anomalous
#     Conditions: v=hZpzr8TbF08 | Video is region-locked
#     Result: HTTP 403 - "hZpzr8TbF08 is not available in your region"
#     """
#     with pytest.raises(HTTPException) as e:
#         video = await verify_availability(v="hZpzr8TbF08")
#     assert str(e.value) == "404: hZpzr8TbF08 is not available in your region"


@pytest.mark.asyncio
async def test_verify_availability_008_anomalous_video_private():
    """
    Test 009 - Anomalous
    Conditions: v=m8uHb5jIGN8 | Video is private
    Result: HTTP 403 - "m8uHb5jIGN8 is a private video"
    """
    with pytest.raises(HTTPException) as e:
        video = await verify_availability(v="m8uHb5jIGN8")
    assert str(e.value) == "403: m8uHb5jIGN8 is a private video"


@pytest.mark.asyncio
async def test_verify_availability_009_anomalous_members_only():
    """
    Test 010 - Anomalous
    Conditions: v=TsX11pJIARc | Video is member's only
    Result: HTTP 404 - "TsX11pJIARc is unavailable"
    """
    with pytest.raises(HTTPException) as e:
        video = await verify_availability(v="TsX11pJIARc")
    assert str(e.value) == "404: TsX11pJIARc is unavailable"
