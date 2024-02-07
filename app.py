"""
app.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Run FastAPI application

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from limiter import limiter

# Create FastAPI client
app = FastAPI()

# Configure rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
