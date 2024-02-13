"""
get_storage_directory.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Get and validate the storage directory from the "STORAGE_DIRECTORY" environment variable

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the Atto-Host project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os


def get_storage_directory():
    storage_directory = os.environ.get("STORAGE_PATH")
    if storage_directory is None:
        raise EnvironmentError(
            "The environment variable 'STORAGE_DIRECTORY' is not set"
        )
    elif not os.path.exists(storage_directory):
        raise FileNotFoundError(
            "The path representent by environment variable 'STORAGE_DIRECTORY' does not exist"
        )
    elif not os.path.isdir(storage_directory):
        raise NotADirectoryError(
            f"The environment variable 'STORAGE_DIRECTORY' does not represent a directory"
        )
    return storage_directory
