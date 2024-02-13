"""
stitch_video.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Stitch an audio and video stream together

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import ffmpeg


async def stitch_video(audio_path, video_path, output_path):
    # Validate that the audio path exists and represents a file
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Could not find file at {audio_path}")
    if not os.path.isdir(audio_path):
        raise IsADirectoryError(f"Path {audio_path} represents a directory, not a file")

    # Validate that the video path exists and represents a file
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Could not find file at {video_path}")
    if not os.path.isdir(video_path):
        raise IsADirectoryError(f"Path {video_path} represents a directory, not a file")

    # Do not allow method to overwrite an existing file
    if os.path.exists(output_path):
        raise FileExistsError(
            f"Path {output_path} already exists and would be overwritten"
        )

    input_audio = ffmpeg.input(audio_path)
    input_video = ffmpeg.input(video_path)
    ffmpeg.output(input_video, input_audio, output_path).run(quiet=True)
    return
