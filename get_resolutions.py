"""
get_resolutions.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Get the available resolutions of a YouTube video

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from pytube.query import StreamQuery
from exceptions import ArgumentError


async def get_resolutions(streams: StreamQuery):
    # Validate the argument 'streams'
    if streams is None:
        raise ArgumentError("Argument 'streams' was None")
    if streams is not None and not isinstance(streams, StreamQuery):
        raise TypeError("Argument 'streams' must be a StreamQuery object")

    # Get a list of the available resolutions
    resolutions = []
    videoStreams = streams.filter(only_video=True)
    for stream in videoStreams:
        if stream.resolution is not None and stream.resolution not in resolutions:
            resolutions.append(stream.resolution)
    print(resolutions)
    return resolutions
