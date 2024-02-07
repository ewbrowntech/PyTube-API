"""
limiter.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Configured rate limiting for the application

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

from slowapi import Limiter
from slowapi.util import get_remote_address

# Create a Limiter instance. The key function is used to determine how to limit requests (by IP in this case).
limiter = Limiter(key_func=get_remote_address)
