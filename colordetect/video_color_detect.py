import sys
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

    def get_video_frames(self, frame_color_count: int = 5, color_format: str = "rgb", progress: bool = False) -> dict:
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
            raise TypeError(
                f"frame_color_count has to be an integer. Provided {type(frame_color_count)} "
            )

        color_format_options = ["rgb", "hex", "hsv"]

        if color_format not in color_format_options:
            raise ValueError(f"Invalid color format: {color_format}")

        if type(progress) != bool:
            raise ValueError(f"Progress should be a boolean. Provided {type(progress)}")

        count = 0
        fps = self.video_file.get(cv2.CAP_PROP_FPS)
        total_frame_count = self.video_file.get(cv2.CAP_PROP_FRAME_COUNT)
        video_duration = float(total_frame_count) / float(fps)
        while self.video_file.isOpened():
            # frame is the image
            success, frame = self.video_file.read()
            if success:
                #  read file every second
                self.video_file.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
                success, image = self.video_file.read()
                image_object = ColorDetect(image)
                colors = image_object.get_color_count(color_count=frame_color_count, color_format=color_format)
                # merge dictionaries as they are created
                self.color_description = {**self.color_description, **colors}
                count += 1
                if count >= video_duration:
                    break
                if progress:
                    self._progress_bar(i=count, total_length=round(video_duration))

        self.video_file.release()
        cv2.destroyAllWindows()
        print("\n")
        return self.color_description

    def color_sort(self, color_count: int = 5, ascending: bool = True):
        """
        color_sort
        ----------------
        Get number of colors wanted from video

        Parameters
        ----------
        color_count: int
            The number of most dominant colors to be obtained from the image
        :return:
        """
        if type(color_count) != int:
            raise TypeError(f"color_count has to be an integer. Provided {type(color_count)} ")

        if type(ascending) != bool:
            raise TypeError(f"The value of the 'ascending' parameter is a boolean. Provided {type(ascending)} ")

        sorted_colors = {
            k: v
            for k, v in sorted(self.color_description.items(), key=lambda item: item[1], reverse=ascending)
        }
        return dict(list(sorted_colors.items())[0:color_count])

    def _progress_bar(self, i, total_length: int, post_text: str = "Color Detection"):
        """display a progress bar of video processing"""
        n_bar = 100
#       # size of progress bar
        j = i / total_length
        sys.stdout.write("\r")
        sys.stdout.write(f"[{'#' * int(n_bar * j):{n_bar}s}] {int(100 *j)}% {post_text}")
        sys.stdout.flush()
