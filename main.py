"""
main.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Run the PyTube frontend for downloading a YouTube video

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the PyTube-API project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
from exceptions import ArgumentError
from get_video import get_video
from get_streams import get_streams
from get_preferred_stream import get_preferred_stream
from download_audio_stream import download_audio_stream
from download_video_stream import download_video_stream
from ffmpeg_utilities.transcode_video import transcode_video
from ffmpeg_utilities.stitch_video import stitch_video
from get_storage_directory import get_storage_directory


async def download_youtube_video(
    v, resolution=None, audio_only=False, video_only=False
):
    if audio_only and video_only:
        raise ArgumentError(
            "Arguments audio_only and video_only and cannot be True simultaneously"
        )

    video = await get_video(v)
    streams = await get_streams(video)

    # Download the audio stream for audio-only and complete video requests
    if not video_only:
        audio_file_id = await download_audio_stream(streams)
        audio_filename = audio_file_id + ".mp3"
        audio_stream_path = os.path.join(get_storage_directory(), audio_filename)
    # Download the video stream for video-only and complete video requests
    elif not audio_only:
        video_file_id, video_file_extension = await download_video_stream(streams)
        video_filename = video_file_id + video_file_extension
        # Give the video stream a temporary name for FFMPEG access
        temp_video_stream_path = os.path.join(
            get_storage_directory(), "video-stream-" + video_filename
        )
        video_stream_path = os.path.join(get_storage_directory(), video_filename)
        await transcode_video(temp_video_stream_path, video_stream_path)

    # For complete video requests, stitch the audio and video streams together
    if not audio_only and not video_only:
        # Give the video stream a temporary name for FFMPEG access
        os.rename(video_stream_path, temp_video_stream_path)

        # Execute the stitch operation
        output_path = video_file_id + video_file_extension
        await stitch_video(audio_stream_path, temp_video_stream_path, output_path)

        # Remove the audio and video streams once complete, as they are no longer needed
        os.remove(audio_stream_path)
        os.remove(temp_video_stream_path)

    # Return the correct path
    if audio_only:
        return audio_filename
    elif video_only:
        return video_filename
    else:
        return video_filename
