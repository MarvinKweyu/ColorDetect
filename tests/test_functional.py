import pytest
# from ...color_detect import main, write_to_picture
# from ...color_detect import ColorDetect
from ..src.color_detect import get_input_image
from unittest import TestCase

"""
Functional tests: from the users perspective
"""
"""
# Tests to be written:

Whether an image is loaded/present in the given folder
whether an image is loaded
test whether text is written to the image

"""

# class TestUserStory():
#     @classmethod
#     def setUpClass():
#         parser = get_input_image()

class TestImageUpload():
    """
    Tests involving image upload to CLI program
    """
    # def __init__(self):
    #     self.image = 'image1.jpg'


    def test_prescence_of_argument(self):
        """
        Test whether there is an argument parsed to the CLI
        * should be testing whether function main receives an argument
        """
        # self.parser = get_input_image()
        # with pytest.raises(SystemExit):
        #     self.parser.parse_args(['../images/image1.jpg'])
        assert(self.image_name == '/images/image1.jpg')



    def test_image_is_used_as_argument(self):
        """
        Ensure that the argument parsed is an image
        """
        pass


class TestImageSaving():
    """
    Tests with image being saved
    """

    def test_image_has_been_saved(self):
        """
        Ensure that 'out.jpg' has been saved to the choice directory
        """
        pass


    def test_text_in_image(self):
        """
        output image should have text 
        """
        pass
    