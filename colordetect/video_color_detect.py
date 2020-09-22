import os
import cv2
from .color_detect import ColorDetect


class VideoColor(ColorDetect):
    """
      Detect and recognize the number of colors in a video
    """
    def __init__(self, video):
        super().__init__(video)
        self.video_file = cv2.VideoCapture(video)

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
                print(f'Frame is of type: {type(frame)}')
                # save frame as JPEG file
                # cv2.imwrite(os.path.join("Random/frame{:d}.jpg".format(count)), frame)
                # image = cv2.imencode(img=frame)
                image_object = ColorDetect(frame)
                image_object.get_color_count()
                image_object.write_color_count()
                storage_path = os.path.join("Random/frame{:d}.jpg".format(count))
                image_name = "frame" + str(count) + ".jpg"
                image_object.save_image("Random", image_name)()
                count += 1

        self.video_file.release()
        cv2.destroyAllWindows()
