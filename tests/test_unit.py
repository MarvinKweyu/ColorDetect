"""
Unit tests: testing a small bit of code like function or class in isolation of the system
From the developers perspective
"""

import mimetypes
import os
from pathlib import Path

import cv2
import pytest

from ..colordetect import ColorDetect, VideoColor, col_share


def test_image_vid_parsed_to_class(image, video):
    """
    test whether an image/video is parsed to the class ColorDetect(<image>)
    Check whether an instance is created
    """
    isinstance(ColorDetect(image), object)
    isinstance(VideoColor(video), object)


def test_color_detect_gets_numpy_array_from_video(image, video):
    """
    Test whether the filename used in the test is the first image
    """
    # user_video = VideoColor(video)
    pass


def test_get_color_count_has_correct_color_and_count(image):
    """
    Ensure get_color_count gets the correct color and count
    """
    user_image = ColorDetect(image)
    # since the image is plain 255,255,255
    assert len(user_image.get_color_count(color_count=1)) == 1
    assert user_image.get_color_count(color_count=1) == {"white": 100.0}


def test_what_is_in_dictionary_is_being_written(datadir, image):
    """
    What is in the dictionary should be what is being written
    """

    user_image = ColorDetect(image)
    # color_dictionary = user_image.get_color_count(color_count=1)
    user_image.get_color_count(color_count=1)
    file_name = "out.jpg"
    user_image.save_image(location=datadir, file_name=file_name)
    # result_image = os.path.join(datadir, file_name)


def test_valid_color_format_is_parsed(image, video):
    """
    An exception is raised if an invalid color_format is parsed
    """
    user_image = ColorDetect(image)
    user_video = VideoColor(video)

    with pytest.raises(Exception):
        user_image.get_color_count(color_count=1, color_format="invalid_random_format")

    with pytest.raises(Exception):
        user_video.get_video_frames(
            frame_color_count=1, color_format="invalid_random_format"
        )

    user_image.get_color_count(color_count=1)
    with pytest.raises(Exception):
        user_image.write_color_count(font_color=(267, 0, 0))


def test_valid_params_to_get_color_count(image):
    """
    An exception is raised if an invalid color_count value is parsed. Instance, a string
    """
    user_image = ColorDetect(image)
    with pytest.raises(Exception):
        user_image.get_color_count(color_count="many_colors")


def test_save_params_are_valid(image, datadir):
    """
    A string is being used as a file name as well as location
    """
    user_image = ColorDetect(image)
    user_image.get_color_count(color_count=1)

    with pytest.raises(Exception):
        user_image.save_image(location=datadir, file_name=5)

    # with pytest.raises(Exception) as e_info:
    #     user_image.save_image(location=500, file_name="output.jpg")


def test_result_file_name_is_valid(image, datadir):
    """
    test result filename has what was given as the file name
    :param image:
    :param datadir:
    :return:
    """
    user_image = ColorDetect(image)
    user_image.get_color_count(color_count=1)
    file_name = "ramble.jpg"
    user_image.save_image(location=datadir, file_name=file_name)
    saved_file = os.path.basename(Path(datadir / file_name))
    assert saved_file == file_name


def test_progress_bar_shows_correct_percentage(video):
    """
    ensure the percentage displayed is correct
    :param video:
    :return:
    """
    # user_video = VideoColor(video)
    # user_video.get_video_frames(progress=True)
    pass


def test_get_video_frames_gets_correct_params(video):
    user_video = VideoColor(video)

    with pytest.raises(Exception):
        user_video.get_video_frames(color_format="invalid_random_format")

    with pytest.raises(Exception):
        user_video.get_video_frames(frame_color_count="1")

    with pytest.raises(Exception):
        user_video.get_video_frames(progress=24)


def test_ordered_colors_are_correct_count(video):
    """
    test sorted colors gets correct params and returns correct color count
    :param video:
    """
    user_video = VideoColor(video)
    all_colors = user_video.get_video_frames()
    with pytest.raises(Exception):
        col_share.sort_order(object_description=all_colors, key_count="5")
    with pytest.raises(Exception):
        col_share.sort_order(object_description=all_colors, ascending="random")

    dominant_colors = col_share.sort_order(object_description=all_colors, key_count=6)
    assert len(dominant_colors) == 6
    """
    below line might fail as colors are grabbed on the second instead of per frame
    hence two consecutive calls might grab diff frames on the same second
    """
    # assert list(dominant_colors.values()) == [68.83, 22.48, 22.22, 21.7, 19.11, 17.77]


def test_validation_of_rgb_is_correct(image):
    """
    test a valid rgb format can be identified
    """
    user_image = ColorDetect(image)
    assert user_image._validate_rgb((255, 0, 0))
    assert not user_image._validate_rgb((256, 0, 0))
    assert not user_image._validate_rgb((255, -2, 0))
