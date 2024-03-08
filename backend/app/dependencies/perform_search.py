"""
perform_search.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Perform a YouTube search using a supplied query

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from pytube import Search
from app.dependencies.get_metadata import get_metadata


async def perform_search(query: str):
    if str is None:
        raise ValueError("No search query was provided")

    # Perform the search
    s = Search(query)

    # For each video in the results, get the metadata
    results = [await get_metadata(video) for video in s.results]

    return results
