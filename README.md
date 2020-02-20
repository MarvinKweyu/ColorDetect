
![Python](https://img.shields.io/badge/Python-3.7-green)
 ![Version](https://img.shields.io/badge/Version-1.0-orange)

Color recognition works to identify different color candies in an image.

### Basic Usage
Create virtual environment and install dependencies
Install dependencies
```bash
pip install -r requirements.txt
```

To count the number of colored candy in an image
```bash
python color_detect.py -i 'path to image'
```
Alternatively
```bash
python color_detect.py --image 'path to image'
```
### Example
```bash
python color_detect.py -i ./images/image1.jpg
```

In the same directory you are running the program a file `out.jpg`
with the color count showing on the image will be created.

-  A sample output.


![Sample image](./images/out.jpg)


#### ToDo

- [ ]  Allow color count in videos.

