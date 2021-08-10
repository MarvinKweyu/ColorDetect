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
import tempfile
from pathlib import Path
from urllib.request import urlopen

import cv2
import matplotlib.colors as mcolors
import numpy as np
import webcolors
from sklearn.cluster import KMeans

from . import col_share

LOGGER = logging.getLogger(__name__)


class ColorDetect:
    """
    Detect and recognize the number of colors in an image
    """

    def __init__(self, image, resize_h: int = None):
        """Create ColorDetect object by providing an image"""

        #  check type of data being passed
        if isinstance(image, np.ndarray):
            self.image = image
        elif isinstance(image, str):
            if col_share.is_url(image) is True:
                img_data = urlopen(image).read()
                dir_name = tempfile.mkdtemp()
                dir_path = Path(dir_name)
                # image saved in a temp dir as img.jpg to be read by colordetect
                dist_file = str(dir_path / "img.jpg")
                f = open(dist_file, "wb")
                f.write(img_data)
                f.close()
                self.image = cv2.imread(dist_file)
            else:
                self.image = cv2.imread(image)
        else:
            raise TypeError(
                "The image parameter accepts a numpy array , string file path or string file url argument only"
            )
        if resize_h is not None:
            h0, w0, _ = self.image.shape
            h1 = resize_h
            w1 = int(w0 * h1 / h0)
            self.image = cv2.resize(self.image, (w1, h1))
        self.image_original = self.image.copy()

        self.color_description = {}

    def get_segmented_image(
        self,
        lower_bound: tuple,
        upper_bound: tuple,
        erode_iterations: int = 3,
        dilate_iterations: int = 3,
        use_grab_cut: bool = True,
        gc_iterations: int = 3,
    ) -> tuple:
        """
        .. _get_segmented_image:
        get_segmented_image
        ---------------
        Get image masks from an image

        Parameters
        ----------
        lower_bound: tuple
            A lower color range from which to look from
        upper_bound: tuple
            The higher RGB color range from which to look from
        erode_iterations: int
            The number of times to perform erosion of the image
        dilate_iterations: int
            The number of times dilation is applied.
        use_grab_cut: bool
            A boolean indicating whether grabCut will be applied to the image. This is True by default.
        gc_iterations: int
            Number of iterations the algorithm should make before returning the result
        :return: output_image, gray, segmented, mask
        """

        if not self._validate_rgb(lower_bound):
            raise TypeError(
                f"lower_bound has to be a tuple of integers. Provided {type(lower_bound)} "
            )
        if not self._validate_rgb(upper_bound):
            raise TypeError(
                f"upper_bound has to be a tuple of integers. Provided {type(upper_bound)} "
            )

        if type(erode_iterations) != int:
            raise TypeError(
                f"erode_iterations has to be an integer. Provided {type(erode_iterations)} "
            )

        if type(dilate_iterations) != int:
            raise TypeError(
                f"dilate_iterations has to be an integer. Provided {type(dilate_iterations)} "
            )

        if type(gc_iterations) != int:
            raise TypeError(
                f"gc_iterations has to be a an integer. Provided {type(gc_iterations)} "
            )
        if type(use_grab_cut) != bool:
            raise TypeError(
                f"use_grab_cut has to be a boolean. Provided {type(use_grab_cut)} "
            )
        gray = cv2.cvtColor(self.image_original, cv2.COLOR_BGR2GRAY)
        output_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        img2 = self.image_original.copy()
        img2 = cv2.GaussianBlur(img2, (11, 11), 0)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(img2, lower_bound, upper_bound)
        mask = cv2.erode(mask, None, iterations=erode_iterations)
        mask = cv2.dilate(mask, None, iterations=dilate_iterations)

        if use_grab_cut:
            mask[mask == 0] = cv2.GC_BGD
            mask[mask > 0] = cv2.GC_PR_FGD

            fg_model = np.zeros((1, 65), dtype="float")
            bg_model = np.zeros((1, 65), dtype="float")

            mask, bg_model, fg_model = cv2.grabCut(
                self.image_original,
                mask,
                None,
                fg_model,
                bg_model,
                iterCount=gc_iterations,
                mode=cv2.GC_INIT_WITH_MASK,
            )
            mask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)
            mask = (mask * 255).astype("uint8")

        segmented = cv2.bitwise_and(self.image_original, self.image_original, mask=mask)

        for i in range(len(mask)):
            for j in range(len(mask[i])):
                if mask[i][j] != 0:
                    output_image[i][j] = self.image_original[i][j]

        return output_image, gray, segmented, mask

    def get_color_count(
        self, color_count: int = 5, color_format: str = "human_readable"
    ) -> dict:
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
                * human_readable - yellow for yellow
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

        color_format_options = ["rgb", "hex", "hsv", "human_readable"]

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

        elif color_format == "human_readable":
            r0, g0, b0 = int(rgb_value[0]), int(rgb_value[1]), int(rgb_value[2])
            try:
                nearest = webcolors.rgb_to_name((r0, g0, b0))
            except ValueError:  # Calculate distances between rgb value and CSS3 rgb colours to determine the closest
                distances = {}
                for k, v in webcolors.CSS3_HEX_TO_NAMES.items():
                    r1, g1, b1 = webcolors.hex_to_rgb(k)
                    distances[
                        ((r0 - r1) ** 2 + (g0 - g1) ** 2 + (b0 - b1) ** 2)
                    ] = v  # Ignore sqrt as it has no significant effect
                nearest = distances[min(distances.keys())]
            return nearest

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

    def write_color_count(
        self,
        left_margin: int = 10,
        top_margin: int = 20,
        font: int = cv2.FONT_HERSHEY_SIMPLEX,
        font_color: tuple = (0, 0, 0),
        font_scale: float = 1.0,
        font_thickness: float = 1,
        line_type: int = 1,
    ):
        """
        .. _write_color_count:
        write_color_count
        -----------------
        Write the number of colors found to the image

        Parameters
        ----------
        left_margin: int
            Text spacing from the left
        top_margin: int
            Text spacing from the top
        font: int
            Font to use in text. Look up acceptable values from python-opencv
        font_color:
            RGB tuple of text font color
        font_scale:
            Size of the text to be written
        font_thickness:
            Thickness of the text
        line_type: int = 1,
        """
        if not self.color_description:
            raise AttributeError(
                "No color description found on this object. Perform get_color_count() first."
            )

        if not self._validate_rgb(font_color):
            raise TypeError(
                f"font_color has to be a tuple of integers. Provided {font_color} "
            )

        for k, v in self.color_description.items():
            color_values = str(v) + "% :" + k
            (text_width, text_height), baseline = cv2.getTextSize(
                color_values, font, font_scale, font_thickness
            )
            # change to BGR color format from RGB tuple
            bgr_color_format = (font_color[2], font_color[1], font_color[0])
            self.write_text(
                text=color_values,
                left_margin=left_margin,
                top_margin=top_margin,
                font=font,
                font_color=bgr_color_format,
                font_scale=font_scale,
                font_thickness=font_thickness,
                line_type=line_type,
            )

            top_margin += text_height

    def write_text(
        self,
        text: str = "",
        left_margin: int = 10,
        top_margin: int = 20,
        font: int = cv2.FONT_HERSHEY_SIMPLEX,
        font_color: tuple = (0, 0, 0),
        font_scale: float = 1.0,
        font_thickness: float = 1.0,
        line_type: int = 1,
        line_spacing: int = 0,
    ):
        """
        .. _write_text:
        write_text
        ----------
        Write text onto an image

         Parameters
        ----------
        text: str
            The text to be written onto the image
        line_spacing:int
            The spacing between lines
        left_margin: int
            Text spacing from the left
        top_margin: int
            Text spacing from the top
        font: int
            Font to use in text. Look up acceptable values from python-opencv
        font_color:
            RGB tuple of text font color
        font_scale:
            Size of the text to be written
        font_thickness: float = 1.0
            Thickness of the text
        line_type: int = 1,
            Space betweeen the lines
        :return:
        """
        if type(text) != str:
            raise TypeError(
                f"text should be a string.Provided {text} of type {type(text)}"
            )

        if text == "":
            raise IOError("text should not be empty")

        if not self._validate_rgb(font_color):
            raise TypeError(
                f"font_color has to be a tuple of integers. Provided {font_color} "
            )

        # change to BGR color format from RGB tuple
        font_color = (font_color[2], font_color[1], font_color[0])

        cv2.putText(
            self.image,
            text,
            (left_margin, top_margin),
            font,
            font_scale,
            font_color,
            font_thickness,
            line_type,
            line_spacing,
        )

    def save_image(self, location=".", file_name: str = "out.jpg"):
        """
        .. _save_image:
        save_image
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

    def _validate_rgb(self, rgb_tuple: tuple) -> bool:
        """
        Validate whether a tuple passed is a valid RGB

        Parameters
        ----------
        rgb_tuple: tuple
            An RGB tuple color.
        :return:
        """
        tuple_made_of_three = isinstance(rgb_tuple, tuple) and len(rgb_tuple) == 3
        tuple_has_integers_only = (
            isinstance(rgb_tuple[0], int)
            and isinstance(rgb_tuple[1], int)
            and isinstance(rgb_tuple[2], int)
        )
        color_range = []

        for color in rgb_tuple:
            if color in range(0, 256):
                color_range.append(True)
            else:
                color_range.append(False)

        invalid_color_range = False in color_range

        return (
            tuple_made_of_three and tuple_has_integers_only and not invalid_color_range
        )
