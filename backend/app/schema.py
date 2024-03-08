"""
schema.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Define schema for use in path operations

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from pydantic import BaseModel, Field


class Query(BaseModel):
    query: str = Field(..., example="Never Gonna Give You Up")
