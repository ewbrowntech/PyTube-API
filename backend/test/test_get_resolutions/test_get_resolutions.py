"""
test_get_resolutions.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Test the functionality of get_resolutions()

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import pytest
from pytube.query import StreamQuery
from fastapi import HTTPException
from app.exceptions import ArgumentError
from app.get_video import get_video
from app.get_streams import get_streams
from app.get_resolutions import get_resolutions


@pytest.mark.asyncio
async def test_get_resolutions_000_nominal():
    """
    Test 000 - Nominal
    Conditions: Streams supplied
    Result: resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]
    """
    video = await get_video(v="SOI4OF7iIr4")
    streams = await get_streams(youtube=video)
    resolutions = await get_resolutions(streams=streams)
    assert resolutions == ["1080p", "720p", "480p", "360p", "240p", "144p"]


@pytest.mark.asyncio
async def test_get_resolutions_001_anomalous_no_input():
    """
    Test 001 - Anomalous
    Conditions: streams = None
    Result: ArgumentError("Argument 'streams' was None")
    """
    streams = None
    with pytest.raises(ArgumentError) as e:
        streams = await get_resolutions(streams=streams)
    assert str(e.value) == "Argument 'streams' was None"


@pytest.mark.asyncio
async def test_get_resolutions_002_anomalous_input_wrong_type():
    """
    Test 002 - Anomalous
    Conditions: streams = "Hi"
    Result: TypeError("Argument 'streams' must be a StreamQuery object")
    """
    streams = "Hi"
    with pytest.raises(TypeError) as e:
        streams = await get_resolutions(streams=streams)
    assert str(e.value) == "Argument 'streams' must be a StreamQuery object"
