import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ColorDetect",
    version="0.1.1",
    author="Marvin Kweyu",
    author_email="mkweyu1@gmail.com",
    description="Detect and get color count in images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarvinKweyu/ColorDetect",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "attrs==19.3.0",
        "importlib-metadata==1.5.0",
        "imutils==0.5.3",
        "more-itertools==8.2.0",
        "numpy==1.18.1",
        "opencv-python==4.2.0.32",
        "packaging==20.1",
        "pluggy==0.13.1",
        "py==1.8.1",
        "pyparsing==2.4.6",
        "pytest==5.3.5",
        "pytest-datafiles==2.0",
        "six==1.14.0",
        "wcwidth==0.1.8",
        "zipp==3.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
