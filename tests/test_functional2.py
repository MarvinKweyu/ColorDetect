
import pytest

# from ..src.color_detect import get_input_image


def test_prescence_of_argument(image):
  """
  Test whether the filename used in the test is the first image
  """
  assert(image == './tests/test_files/image2.jpg') 
 

def test_argument_is_image(image):
        """
        Ensure that the argument parsed is an image
        """
        print(image)