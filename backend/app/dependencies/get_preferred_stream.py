"""
get_preffered_stream.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Get the stream with the most compatible codec for a given resolution

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from pytube.query import StreamQuery
from app.dependencies.exceptions import ArgumentError, UnvailableResolutionException


async def get_preferred_stream(streams: StreamQuery, resolution: str):
    # Validate the argument 'streams'
    if streams is None:
        raise ArgumentError("Argument 'streams' was None")
    if streams is not None and not isinstance(streams, StreamQuery):
        raise TypeError(
            f"Argument 'streams' must be a StreamQuery object, not {type(streams)}"
        )

    # Validate the argument 'resolutions'
    if resolution is None:
        raise ArgumentError("Argument 'resolution' was None")
    if resolution is not None and not isinstance(resolution, str):
        raise TypeError(
            f"Argument 'resolution' must be a string, not {type(resolution)} (EX: '480p')"
        )

    # Filter out any streams that do not match the intended resolution
    acceptable_streams = [
        stream for stream in streams if stream.resolution == resolution
    ]
    if len(acceptable_streams) == 0:
        raise UnvailableResolutionException(resolution=resolution)

    # Filter of most easily transcoded codecs, in the following order:
    # 1) VP9
    preferred_streams = [
        stream for stream in acceptable_streams if "vp9" in stream.codecs[0]
    ]
    # 2) AVC
    if preferred_streams == []:
        preferred_streams = [
            stream for stream in acceptable_streams if "avc" in stream.codecs[0]
        ]
    # 3) AV1
    if preferred_streams == []:
        preferred_streams = [
            stream for stream in acceptable_streams if "av01" in stream.codecs[0]
        ]
    if preferred_streams == []:
        raise Exception(
            f"There where no streams at the resolution of {resolution} encoded in VP9, AVC, or AV1"
        )

    # Return the most applicable stream
    return preferred_streams[0]
