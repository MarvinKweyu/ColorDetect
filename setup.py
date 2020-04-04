import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ColorDetect",
    version="0.1.3",
    author="Marvin Kweyu",
    author_email="mkweyu1@gmail.com",
    description="Detect and get color count in images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarvinKweyu/ColorDetect",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=[
        "numpy==1.18.1",
        "opencv-python==4.2.0.32",
        "imutils==0.5.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
