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

    
