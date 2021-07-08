"""
.. _module_VideoColor:
Module VideoColor
==================
Defines VideoColor class

Usage:

>>> from colordetect import VideoColor
>>> user_video = VideoColor("<path_to_video>")
# where frame_color_count is the target most dominant colors to be found. Default set to 5
>>> colors =  user_video.get_video_frames(frame_color_count=7)
>>> colors
# alternatively shorten the dictionary to get a specific number of sorted colors from the whole lot
>>> from colordetect import col_share
>>> top_colors = col_share.sort_order(object_description=colors, key_count=8)
"""

import sys

import cv2

from . import col_share
from .color_detect import ColorDetect


class VideoColor:
    """
    Detect and recognize the number of colors in a video
    """

    def __init__(self, video):
        # super().__init__(video)
        self.video_file = cv2.VideoCapture(video)
        self.color_description = {}

    def get_video_frames(
        self,
        frame_color_count: int = 5,
        color_format: str = "rgb",
        progress: bool = False,
    ) -> dict:
        """
        .. _get_video_frames:
        get_video_frames
        ----------------
        Get image frames and their colors from the video

        Parameters
        ----------
        frame_color_count: int
            The number of most dominant colors to be obtained from a single frame
        color_format:str
            The format to return the color in.
            Options
                * hsv - (60°,100%,100%)
                * rgb - rgb(255, 255, 0) for yellow
                * hex - #FFFF00 for yellow
          :return: color_description dictionary
        """
        if type(frame_color_count) != int:
            raise TypeError(
                f"frame_color_count has to be an integer. Provided {type(frame_color_count)} "
            )

        color_format_options = ["rgb", "hex", "hsv"]

        if color_format not in color_format_options:
            raise ValueError(f"Invalid color format: {color_format}")

        if type(progress) != bool:
            raise ValueError(f"Progress should be a boolean. Provided {type(progress)}")

        count = 0
        total_frame_count = self.video_file.get(cv2.CAP_PROP_FRAME_COUNT)
        while self.video_file.isOpened():
            #  read file every second
            self.video_file.set(cv2.CAP_PROP_POS_MSEC, count * 1000)
            success, image = self.video_file.read()
            if not success:
                break  # Video is complete
            image_object = ColorDetect(image)
            colors = image_object.get_color_count(
                color_count=frame_color_count, color_format=color_format
            )
            # merge dictionaries as they are created
            self.color_description = {**self.color_description, **colors}
            count += 1
            current_frame_num = self.video_file.get(cv2.CAP_PROP_POS_FRAMES)
            if progress:
                col_share.progress_bar(
                    position=current_frame_num, total_length=total_frame_count
                )
        if progress:
            col_share.progress_bar(
                position=total_frame_count, total_length=total_frame_count
            )  # Cater for video with extra millis at the end that don't sum upto a full sec, and are thus skipped

        self.video_file.release()
        print("\n")
        return self.color_description
