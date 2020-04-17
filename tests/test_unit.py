"""
Unit tests: testing a small bit of code like function or class in isolation of the system
From the developers perspective
"""

import os

import pytest

from ..colordetect import ColorDetect


def test_image_parsed_to_class(image):
    """
    test whether an image is parsed to the class ColorDetect(<image>)
    Check whether an instance is created
    """
    isinstance(ColorDetect(image), object)


def test_dictionary_has_correct_color_count(image):
    """
    Ensure the method gets the correct color count
    """
    user_image = ColorDetect(image)
    # since the image is plain 255,255,255
    assert len(user_image.get_color_count(color_count=1)) == 1


def test_what_is_in_dictionary_is_being_written(datadir, image):
    """
    What is in the dictionary should be what is being written
    """
    user_image = ColorDetect(image)
    color_dictionary = user_image.get_color_count(color_count=1)


def test_valid_color_format_is_parsed(image):
    """
    An exception is raised if an invalid color_format is parsed
    """
    user_image = ColorDetect(image)
    with pytest.raises(Exception) as e_info:
        user_image.get_color_count(color_count=1, color_format='invalid_random_format')


def test_valid_color_count_value(image):
    """
       An exception is raised if an invalid color_count value is parsed. Instance, a string
       """
    user_image = ColorDetect(image)
    with pytest.raises(Exception) as e_info:
        user_image.get_color_count(color_count="many_colors")


def test_result_file_name_is_valid(image, datadir):
    """
    A string is being used as a file name
    """
    user_image = ColorDetect(image)
    user_image.get_color_count(color_count=1)

    with pytest.raises(Exception) as e_info:
        user_image.save_color_count(location=datadir, file_name=5)