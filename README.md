# ColorDetect


[![PyPI version](https://badge.fury.io/py/ColorDetect.svg)](https://pypi.org/project/ColorDetect/)
[![CircleCI](https://circleci.com/gh/MarvinKweyu/ColorDetect.svg?style=svg)](https://circleci.com/gh/MarvinKweyu/ColorDetect)
[![Downloads](https://pepy.tech/badge/colordetect)](https://pypi.org/project/ColorDetect/)


ColorDetect works to recognize and identify different colors in an image.


### Installation

```bash
pip install ColorDetect
```

### Basic Usage
```python
from colordetect import ColorDetect


user_image = ColorDetect(<path_to_image>)
# get a dictionary return of color count
user_image.get_color_count()
# save the color count onto the image
user_image.save_color_count(<storage_path>,<image_name>)

```

Resultant image is stored in the string `storage_path` of choice with the `image_name` which will default to the current location and **out.jpg** respectively by default.

### Project Documentation

For further project documentation, visit [ColorDetect's page](https://colordetect.readthedocs.io/en/latest/) 

### Contributions

Contributions are welcome.
Do remember to take a look at the project [contribution guidelines](CONTRIBUTING.rst)

#### Tests
To run tests:
```bash
pytest 
```
