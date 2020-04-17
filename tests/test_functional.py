import imghdr
from pathlib import Path
from unittest import TestCase

import pytest

from ..colordetect import ColorDetect

"""
# Tests to be written:

Whether an image is loaded/present in the given folder
whether an image is loaded
test whether text is written to the image

"""


def test_existence_of_image_path(image):
    """
  Test whether the filename used in the test is the first image
  """
    assert (Path(image).exists())


def test_argument_is_image(image):
    """
        Ensure that the argument parsed is an image
        """
    assert type(imghdr.what(Path(image))) is str


def test_image_has_been_saved(datadir, image):
    """
        Ensure that 'out.jpg' has been saved to the choice directory
        """
    user_image = ColorDetect(image)
    user_image.get_color_count(color_count=1)
    file_name = 'out.jpg'
    user_image.save_color_count(location=datadir, file_name=file_name)
    assert (Path(datadir / file_name).exists())


def test_correct_color_format(image):
    """
    What user specified is the color format to be written is being written
    :param image:
    :return:
    """
    pass


def test_text_in_image(datadir):
    """
    output image should have text 
    """
    pass
