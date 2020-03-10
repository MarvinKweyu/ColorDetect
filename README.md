
![Python](https://img.shields.io/badge/Python-3.7-green)
![Release](https://img.shields.io/github/v/release/MarvinKweyu/ColorRecognition?include_prereleases)
![Downloads](https://img.shields.io/github/downloads/MarvinKweyu/ColorRecognition/total?style=flat)

ColorDetect works to identify different color candies in an image.



 ### Table of Contents

 [ Basic Usage](#Setup)
 
 [ Download](#Download)

 [Contributions](#Contributions)

 [License](#License)

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


#### Tests
To run tests:
```bash
pytest tests --image ./tests/test_files/image2.jpg
```


### Download
Get the latest release from the [release page](https://github.com/MarvinKweyu/ColorRecognition/releases)


### Contributions

Contributions are welcome.
Do remember to take a look at the project [contribution guidelines](./CONTRIBUTING.md)


#### ToDo
- [ ]  Let the user save the file as they want/ save with detault file_name.
- [ ]  Allow color count in videos.
