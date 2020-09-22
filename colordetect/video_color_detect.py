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

    def get_video_frames(self):
        """
         Get image frames from the video
          :return:
        """
        count = 0
        while self.video_file.isOpened():
            # frame is the image
            success, frame = self.video_file.read()
            if success:
                # save frame as JPEG file
                image_object = ColorDetect(frame)
                colors = image_object.get_color_count()
                # merge dictionaries as they are created
                self.color_description = {**self.color_description, **colors}
                # image_object.write_color_count()
                # storage_path = os.path.join("Random/frame{:d}.jpg".format(count))
                # image_name = "frame" + str(count) + ".jpg"
                # image_object.save_image("Random", image_name)
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
