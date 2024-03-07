"""
test_get_preffered_stream.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Test the functionality of get_preferred_stream()

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import pytest
from fastapi import HTTPException
from app.exceptions import ArgumentError, UnvailableResolutionException
from app.get_video import get_video
from app.get_streams import get_streams
from app.get_preferred_stream import get_preferred_stream


@pytest.mark.asyncio
async def test_get_preffered_stream_000_nominal(test_streams):
    """
    Test 000 - Nominal
    Conditions: v=u15tEo0wsQI | resolution = "2160p" | Streams and resolution supplied
    Result: stream codec = vp9
    """
    preferred_stream = await get_preferred_stream(
        streams=test_streams, resolution="2160p"
    )
    assert preferred_stream is not None
    assert "vp9" in preferred_stream.codecs[0]


@pytest.mark.asyncio
async def test_get_preffered_stream_001_anomalous_streams_none():
    """
    Test 001 - Anomalous
    Conditions: streams = None
    Result: ArgumentError("Argument 'streams' was None")
    """
    with pytest.raises(ArgumentError) as e:
        preferred_stream = await get_preferred_stream(streams=None, resolution="2160p")
    assert str(e.value) == "Argument 'streams' was None"


@pytest.mark.asyncio
async def test_get_preffered_stream_002_anomalous_streams_wrong_type():
    """
    Test 002 - Anomalous
    Conditions: streams = None
    Result: TypeError("Argument 'streams' must be a StreamQuery object, not <class 'str'>")
    """
    with pytest.raises(TypeError) as e:
        preferred_stream = await get_preferred_stream(streams="Hi", resolution="2160p")
    assert (
        str(e.value)
        == "Argument 'streams' must be a StreamQuery object, not <class 'str'>"
    )


@pytest.mark.asyncio
async def test_get_preffered_stream_003_anomalous_resolution_none(test_streams):
    """
    Test 003 - Anomalous
    Conditions: streams = None
    Result: ArgumentError("Argument 'resolution' was None")
    """
    with pytest.raises(ArgumentError) as e:
        preferred_stream = await get_preferred_stream(
            streams=test_streams, resolution=None
        )
    assert str(e.value) == "Argument 'resolution' was None"


@pytest.mark.asyncio
async def test_get_preffered_stream_004_anomalous_resolution_wrong_type(test_streams):
    """
    Test 004 - Anomalous
    Conditions: streams = None
    Result: TypeError("Argument 'resolution' must be a string, not <class 'int'> (EX: '480p')")
    """
    with pytest.raises(TypeError) as e:
        preferred_stream = await get_preferred_stream(
            streams=test_streams, resolution=2160
        )
    assert (
        str(e.value)
        == "Argument 'resolution' must be a string, not <class 'int'> (EX: '480p')"
    )


@pytest.mark.asyncio
async def test_get_preffered_stream_005_anomalous_unavailable_resolution():
    """
    Test 005 - Anomalous
    Conditions: v=_suW-XIX_sQ | resolution = "2160p"
    Result: UnavailableResolutionException("No stream is available at request resolution of 2160p")
    """
    video = await get_video(v="_suW-XIX_sQ")
    streams = await get_streams(youtube=video)
    with pytest.raises(UnvailableResolutionException) as e:
        preferred_stream = await get_preferred_stream(
            streams=streams, resolution="2160p"
        )
    assert str(e.value) == "No stream is available at request resolution of 2160p"
