"""
test_get_video.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Test functionality of get_video() [GET /videos]

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import pytest


@pytest.mark.asyncio
async def test_get_video_001_anomalous_no_video_id(test_client):
    """
    Test 001 - Anomalous
    Conditions: No video ID is provided in query parameter
    Result: HTTP 400 - "Query paramater 'v' for video ID is required"
    """
    response = test_client.get("video")
    assert response.status_code == 400
    assert response.json()["detail"] == "Query paramater 'v' for video ID is required"
