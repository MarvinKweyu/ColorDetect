import os
import itertools
import cv2
from .color_detect import ColorDetect


class VideoColor(ColorDetect):
    """
      Detect and recognize the number of colors in a video
    """
    def __init__(self, video):
        super().__init__(video)
        self.video_file = cv2.VideoCapture(video)
        self.color_description = {}

    def get_video_frames(self, frame_color_count: int = 5, color_format: str = 'rgb') -> dict:
        """
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
          :return:
        """
        if type(frame_color_count) != int:
            raise TypeError(f"frame_color_count has to be an integer. Provided {type(frame_color_count)} ")

        color_format_options = ['rgb', 'hex', 'hsv']

        if color_format not in color_format_options:
            raise ValueError(f"Invalid color format: {color_format}")

        count = 0
        while self.video_file.isOpened():
            # frame is the image
            success, frame = self.video_file.read()
            if success:
                # save frame as JPEG file
                image_object = ColorDetect(frame)
                colors = image_object.get_color_count(color_count=frame_color_count, color_format=color_format)
                # merge dictionaries as they are created
                self.color_description = {**self.color_description, **colors}
                # print(f'{self.color_description}')
                count += 1

        self.video_file.release()
        cv2.destroyAllWindows()
        return self.color_description

    def sorted_colors(self, color_count: int = 5):
        """
        Get number of colors wanted from video
        :return:
        """
        sorted_colors = {k: v for k, v in sorted(self.color_description.items(), key=lambda item: item[1])}
        return dict(list(sorted_colors.items())[0: color_count])
