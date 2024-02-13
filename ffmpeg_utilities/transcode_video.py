"""
transcode_video.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Transcode a video into H264 for compatibility with a greater number of systems

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import ffmpeg


async def transcode_video(input_path, output_path):
    # Validate that the input path exists and represents a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Could not find file at {input_path}")
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Path {input_path} represents a directory, not a file")

    # Do not allow method to overwrite an existing file
    if os.path.exists(output_path):
        raise FileExistsError(
            f"Path {output_path} already exists and would be overwritten"
        )

    ffmpeg.input(input_path).output(output_path, codec="h264").run(quiet=True)
    return
