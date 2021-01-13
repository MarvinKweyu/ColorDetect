from __future__ import unicode_literals

import os
from distutils import dir_util

import pytest


@pytest.fixture(scope="session")
def image(request):
    """
    parse the argument in the test else let the tests skip
    """
    image_value = "tests/test_files/plain-white-background.jpg"
    if image_value is None:
        pytest.skip()
    return image_value  # the image file name


@pytest.fixture(scope="session")
def video(request):
    """
    parse video to test else skip
    :param request:
    :return:
    """
    video_value = "tests/test_files/earth.mp4"

    if video_value is None:
        pytest.skip()
    return video_value


@pytest.fixture
def datadir(tmpdir, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, bytes(tmpdir))

    return tmpdir
