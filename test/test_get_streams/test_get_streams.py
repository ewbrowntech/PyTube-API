"""
test_get_streams.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Test the functionality of get_streams()

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import pytest
from pytube.query import StreamQuery
from fastapi import HTTPException
from exceptions import ArgumentError
from get_video import get_video
from get_streams import get_streams


@pytest.mark.asyncio
async def test_get_streams_000_nominal():
    """
    Test 000 - Nominal
    Conditions: v=SOI4OF7iIr4
    Result: Streams returned
    """
    youtube = await get_video(v="_suW-XIX_sQ")
    streams = await get_streams(youtube=youtube)
    assert isinstance(streams, StreamQuery)


@pytest.mark.asyncio
async def test_get_streams_001_anomalous_no_input():
    """
    Test 001 - Anomalous
    Conditions: youtube = None
    Result: ArgumentError("Argument 'youtube' was None")
    """
    youtube = None
    with pytest.raises(ArgumentError) as e:
        streams = await get_streams(youtube=youtube)
    assert str(e.value) == "Argument 'youtube' was None"


@pytest.mark.asyncio
async def test_get_streams_002_anomalous_input_wrong_type():
    """
    Test 002 - Anomalous
    Conditions: youtube = "Hi"
    Result: ArgumentError("Argument 'youtube' was None")
    """
    youtube = "Hi"
    with pytest.raises(TypeError) as e:
        streams = await get_streams(youtube=youtube)
    assert str(e.value) == "Argument 'youtube' must be a YouTube object"


@pytest.mark.asyncio
async def test_get_streams_003_anomalous_age_restricted():
    """
    Test 003 - Anomalous
    Conditions: v=95_33ItUC9k | Video is age restricted
    Result: HTTPException("401: 95_33ItUC9k is age restricted, and can't be accessed without logging in.")

    """
    video = await get_video(v="95_33ItUC9k")
    with pytest.raises(HTTPException) as e:
        streams = await get_streams(youtube=video)
    assert (
        str(e.value)
        == "401: 95_33ItUC9k is age restricted, and can't be accessed without logging in."
    )
