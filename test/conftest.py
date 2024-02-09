"""
conftest.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Set up fixtures for PyTest

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import pytest_asyncio


@pytest_asyncio.fixture(scope="function")
async def test_client():
    """
    Generate and yield a test client for use in unit tests
    """
    from app import app
    from fastapi.testclient import TestClient

    test_client = TestClient(app)
    yield test_client
