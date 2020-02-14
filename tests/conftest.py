import pytest

def pytest_addoption(parser):
    """
    Store this parse into all the rtest of the tests
    """
    parser.addoption("--image", action="store")


@pytest.fixture(scope='session')
def image(request):
    """
    parse the argument in the test else let the tests skip
    """
    image_value = request.config.option.image
    if image_value is None:
        pytest.skip()
    return image_value # the image file name