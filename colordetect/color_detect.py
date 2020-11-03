"""
.. _module_ColorDetect:
Module ColorDetect
==================
Defines ColorDetect class

For example:

>>> from colordetect import ColorDetect
>>> user_image = ColorDetect("<path_to_image>")
# where color_count is the target most dominant colors to be found. Default set to 5
>>> colors =  user_image.get_color_count(color_count=5)
>>> colors
# alternatively, save these RGB values to the image
>>> user_image.write_color_count()
>>> user_image.save_image("<storage_path>","<image_file_name>")
# Image processed and saved successfully
"""

import logging
from pathlib import Path

import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.colors as mcolors
from . import col_share

LOGGER = logging.getLogger(__name__)


class ColorDetect:
    """
    Detect and recognize the number of colors in an image
    """

    def __init__(self, image):
        """Create ColorDetect object by providing an image"""

        #  check type of data being passed
        if isinstance(image, np.ndarray):
            self.image = image
        else:
            self.image = cv2.imread(image)

        self.color_description = {}

    def get_color_count(self, color_count: int = 5, color_format: str = "rgb") -> dict:
        """
        .. _get_color_count:
        get_color_count
        ---------------
        Count the number of different colors


        Parameters
        ----------
        color_count: int
            The number of most dominant colors to be obtained from the image
        color_format:str
            The format to return  the color in.
            Options
                * hsv - (60°,100%,100%)
                * rgb - rgb(255, 255, 0) for yellow
                * hex - #FFFF00 for yellow
        :return: color description
        """

        if type(color_count) != int:
            raise TypeError(
                f"color_count has to be an integer. Provided {type(color_count)} "
            )

        # convert image from BGR to RGB for better accuracy
        rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        reshape = rgb.reshape((rgb.shape[0] * rgb.shape[1], 3))
        cluster = KMeans(n_clusters=color_count).fit(reshape)

        unique_colors = self._find_unique_colors(cluster, cluster.cluster_centers_)

        color_format_options = ["rgb", "hex", "hsv"]

        if color_format not in color_format_options:
            raise ValueError(f"Invalid color format: {color_format}")

        # round  up figures
        for percentage, v in unique_colors.items():
            rgb_value = list(np.around(v))
            if color_format != "rgb":
                color_value = self._format_color(v, color_format)
                self.color_description[color_value] = round(percentage, 2)
            else:
                self.color_description[str(rgb_value)] = round(percentage, 2)

        return self.color_description

    def _format_color(self, rgb_value, color_format: str):
        """
        Get the correct color format as specified
        :return:
        """
        if color_format == "hsv":
            # list(np.around(v))
            return str(mcolors.rgb_to_hsv(rgb_value).tolist())

        elif color_format == "hex":
            rgb_value = np.divide(rgb_value, 255)  # give a scale from 0-1
            return mcolors.to_hex(rgb_value)

    def _find_unique_colors(self, cluster, centroids) -> dict:

        # Get the number of different clusters, create histogram, and normalize
        labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
        (hist, _) = np.histogram(cluster.labels_, bins=labels)
        hist = hist.astype("float")
        hist /= hist.sum()

        # iterate through each cluster's color and percentage
        colors = sorted(
            [((percent * 100), color) for (percent, color) in zip(hist, centroids)]
        )

        for (percent, color) in colors:
            color.astype("uint8").tolist()
        return dict(colors)

    def write_color_count(self):
        """
        write_color_count
        -----------------
        Write the number of colors found to the image
        """
        if not self.color_description:
            raise AttributeError(
                f"No color description found on this object. Perform get_color_count() first."
            )
        line_spacing = 0
        for k, v in self.color_description.items():
            color_values = str(v) + "% :" + k
            self.write_text(text=color_values, line_spacing=line_spacing)

            line_spacing += 23

    def write_text(self, text: str = "", line_spacing: int = 0):
        """
        write_text
        ----------
        Write text onto an image

         Parameters
        ----------
        text: str
            The text to be written onto the image
        line_spacing:int
            The spacing between lines
        :return:
        """
        if type(text) != str:
            raise TypeError(
                f"text should be a string.Provided {text} of type {type(text)}"
            )

        if text == "":
            raise IOError(f"text should not be empty")

        y_axis = 200 + line_spacing

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, y_axis)
        fontScale = 1
        fontColor = (0, 0, 0)
        lineType = 1

        cv2.putText(
            self.image,
            text,
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType,
        )

    def save_image(self, location=".", file_name: str = "out.jpg"):
        """
        .. _save_color_count:
        save_color_count
        ----------------

        Save the resultant image file to the local directory

        Parameters
        ----------
        location: str
            The file location of the image
        file_name:str
            The name of the new image

        """
        if type(file_name) != str:
            raise TypeError(f"file_name should be a string.Provided {type(file_name)}")

        image_folder = Path(location)
        image_to_save = image_folder / file_name

        # Save image
        cv2.imwrite(str(image_to_save), self.image)

        LOGGER.info("Image processed and saved successfully")
