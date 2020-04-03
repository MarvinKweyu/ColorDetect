from pathlib import Path

import cv2
import imutils
import numpy as np


class ColorDetect:
    """
    Detect and write the number of colors in an image
    """

    def __init__(self, image):
        """Class constructor"""
        self.image = cv2.imread(image)

        # Dictionaries of colors
        self.colors = {
            'red': [
                ([0, 50, 50], [10, 255, 255]),
                ([170, 50, 50], [180, 255, 255])
            ],
            'blue': [
                ([110, 50, 50], [130, 255, 255])
            ],
            'green': [
                ([50, 50, 50], [80, 255, 255])
            ],
            'yellow': [
                ([26, 100, 100], [35, 255, 255])
            ],
            'orange': [
                ([10, 50, 50], [22, 255, 255])
            ],
            'purple': [
                ([140, 50, 0], [165, 255, 255])
            ],
            'cyan': [
                ([80, 50, 50], [100, 255, 255])
            ],
            'lightgreen': [
                ([35, 50, 50], [45, 255, 255])
            ]

        }

        self.color_description = {}

    def get_color_count(self) -> dict:
        """
        Count the number of different colors
        """

        # convert image from BGR to HSV for better accuracy
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        for color, boundaries in self.colors.items():

            i = 0
            for (lower, upper) in boundaries:

                # find all the 'color' shapes in the image
                lower = np.array(lower, dtype="uint8")
                upper = np.array(upper, dtype="uint8")
                shapeMask = cv2.inRange(hsv, lower, upper)

                if i == 0:
                    result = shapeMask
                else:
                    result = cv2.bitwise_or(result, shapeMask)

                i += 1

            # find the contours in the mask
            cnts = cv2.findContours(result.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            self.color_description[color] = len(cnts)

        return self.color_description

    def write_color_count(self):
        """
        Write the number of colors found to the image
        """
        y_axis = 200
        for k, v in self.color_description.items():
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, y_axis)
            fontScale = 1
            fontColor = (0, 0, 0)
            lineType = 1

            cv2.putText(self.image, k + ':' + str(v),
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
            y_axis += 23

    def save_color_count(self, location=".", file_name="out.jpg"):
        """
        Save the resultant image file to the local directory
        
        Parameters
        ----------
        location: str
            The file location of the image
        file_name:str
            The name of the new image

        """
        # write image colors to the image
        self.write_color_count()

        image_folder = Path(location)
        image_to_save = image_folder / file_name

        # Save image
        cv2.imwrite(str(image_to_save), self.image)

        print("Image processed and saved successfully")
