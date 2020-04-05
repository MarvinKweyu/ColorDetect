
from pathlib import Path
import imghdr
from unittest import TestCase

import pytest

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
  assert(Path(image).exists())
 

def test_argument_is_image(image):
        """
        Ensure that the argument parsed is an image
        """
        assert type(imghdr.what(Path(image))) is str


def test_image_has_been_saved(datadir):
        """
        Ensure that 'out.jpg' has been saved to the choice directory
        """
        # image = Path(image)
        pass


def test_text_in_image(datadir):
    """
    output image should have text 
    """
    pass
