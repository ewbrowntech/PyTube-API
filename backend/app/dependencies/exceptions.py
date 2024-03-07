"""
exceptions.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Define custom exceptions

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""


class ArgumentError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class UnvailableResolutionException(Exception):
    def __init__(self, resolution):
        self.message = f"No stream is available at request resolution of {resolution}"
        super().__init__(self.message)
