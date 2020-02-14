
import pytest
# from ..src.color_detect import get_input_image


def test_prescence_of_argument(image):
  """
  Test whether the filename used in the test is the first image
  """
  assert(image == '/images/image1.jpg')