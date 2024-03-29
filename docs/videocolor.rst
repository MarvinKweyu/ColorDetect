.. _video_color_recognition:
Video color recognition
=======================

Full video color detection 
--------------------------

To show how video color recognition works, the following video of planet earth will be used.

.. raw:: html

    <video controls src="_static/earth.mp4"></video>

::

    >>> from colordetect import VideoColor
    >>> my_video = VideoColor("<video_path>")
    >>> my_video.get_video_frames()
    {'[137.0, 165.0, 182.0]': 0.92, '[71.0, 84.0, 95.0]': 2.16, '[24.0, 30.0, 50.0]': 11.17, '[7.0, 10.0, 26.0]': 17.72, '[0.0, 0.0, 0.0]': 68.83, '[143.0, 170.0, 186.0]': 0.85, '[76.0, 89.0, 100.0]': 2.11, '[26.0, 32.0, 52.0]': 11.07, '[8.0, 11.0, 27.0]': 15.71, '[135.0, 163.0, 181.0]': 0.95, '[76.0, 88.0, 98.0]': 2.05, '[127.0, 160.0, 180.0]': 0.94, '[71.0, 83.0, 95.0]': 2.38, '[7.0, 11.0, 27.0]': 15.72, '[124.0, 159.0, 181.0]': 0.9, '[69.0, 83.0, 95.0]': 2.28, '[26.0, 32.0, 53.0]': 13.73, '[125.0, 160.0, 182.0]': 0.89, '[68.0, 82.0, 95.0]': 2.27, '[132.0, 166.0, 187.0]': 0.79, '[71.0, 87.0, 100.0]': 2.1, '[25.0, 32.0, 52.0]': 14.18, '[134.0, 167.0, 186.0]': 0.83, '[72.0, 87.0, 100.0]': 2.01, '[26.0, 33.0, 53.0]': 12.11, '[132.0, 165.0, 183.0]': 0.9, '[73.0, 88.0, 99.0]': 2.04, '[8.0, 10.0, 27.0]': 16.76, '[134.0, 166.0, 184.0]': 0.87, '[132.0, 165.0, 185.0]': 0.86, '[74.0, 89.0, 100.0]': 2.0, '[26.0, 33.0, 52.0]': 10.65, '[7.0, 10.0, 27.0]': 16.93, '[124.0, 157.0, 178.0]': 0.99, '[68.0, 81.0, 93.0]': 2.14, '[25.0, 31.0, 50.0]': 10.66, '[124.0, 160.0, 182.0]': 0.88, '[67.0, 82.0, 94.0]': 2.19, '[25.0, 31.0, 49.0]': 10.68, '[124.0, 160.0, 183.0]': 0.85, '[67.0, 83.0, 95.0]': 2.0, '[25.0, 30.0, 49.0]': 11.04, '[123.0, 160.0, 182.0]': 0.87, '[24.0, 29.0, 47.0]': 9.51, '[23.0, 29.0, 47.0]': 10.6, '[6.0, 9.0, 26.0]': 19.11, '[67.0, 83.0, 97.0]': 2.0, '[24.0, 29.0, 48.0]': 9.83, '[125.0, 161.0, 183.0]': 0.88, '[67.0, 83.0, 96.0]': 1.96, '[127.0, 162.0, 183.0]': 0.87, '[23.0, 29.0, 46.0]': 8.58, '[5.0, 8.0, 25.0]': 17.77, '[68.0, 84.0, 98.0]': 1.9, '[24.0, 29.0, 46.0]': 6.95, '[125.0, 161.0, 184.0]': 0.85, '[67.0, 84.0, 99.0]': 1.89, '[133.0, 165.0, 186.0]': 0.82, '[67.0, 85.0, 99.0]': 1.84, '[23.0, 28.0, 45.0]': 6.83, '[5.0, 8.0, 24.0]': 22.22, '[135.0, 165.0, 186.0]': 0.85, '[69.0, 86.0, 100.0]': 1.79, '[22.0, 27.0, 43.0]': 7.22, '[5.0, 7.0, 24.0]': 22.48, '[133.0, 166.0, 186.0]': 0.81, '[73.0, 91.0, 105.0]': 1.69, '[129.0, 163.0, 185.0]': 0.85, '[69.0, 86.0, 98.0]': 1.9, '[21.0, 27.0, 44.0]': 7.25, '[4.0, 7.0, 24.0]': 21.7, '[68.0, 86.0, 101.0]': 1.9, '[22.0, 27.0, 45.0]': 7.91, '[126.0, 160.0, 181.0]': 0.94, '[66.0, 83.0, 96.0]': 1.91, '[22.0, 27.0, 46.0]': 9.19, '[129.0, 163.0, 184.0]': 0.86, '[68.0, 85.0, 98.0]': 2.01, '[21.0, 27.0, 46.0]': 10.62, '[133.0, 165.0, 185.0]': 0.85, '[69.0, 86.0, 99.0]': 1.96, '[23.0, 29.0, 48.0]': 10.61, '[7.0, 9.0, 26.0]': 17.7, '[135.0, 165.0, 185.0]': 0.85, '[73.0, 88.0, 100.0]': 1.96, '[24.0, 29.0, 50.0]': 11.34, '[139.0, 164.0, 177.0]': 0.92}

Just as image color recognition, a dictionary will be returned.
:ref:`get_video_frames<get_video_frames>` takes optional parameters, that is, `frame_color_count`, an integer describing how many colors to get per frame
grabbed, and `color_format`, working much the same way as :ref:`get_color_count<get_color_count>`, which is to say either RGB, HSV or hex values.

Depending on the video, you may want to display progress of the processing. Thus, an additional, optional parameter, ``progress=True`` may be included.
This is **False** by default.

Colors are grabbed on a per second basis. Hence , in a video 30 seconds long, a single frame will be used for each second of feed.

Have a look at :ref:`col_share<col_share>` for details into how you may format the results.


Working with videos and time
----------------------------

We can get colors at specific times of the parsed video

::

   >>> from colordetect import VideoColor
   >>> my_video = VideoColor("<video_path>")
   >>> (image, color_description) = my_video.get_time_frame_color(time=15000)

The result is a tuple with a ColorDetect object and a color description. 
We can proceed to save the color description onto the image in our preferred color

::

    >>> image.write_color_count(font_color=(255,255,255), save=True)


Locate a file `out.jpg` in your current working directory.


We could, **alternatively**, handle the saving ourselves and go as below:
::


    >>> image.write_color_count(font_color=(255,255,255))
    >>> image.save_image(location='path/to/directory/of/choice', filename='filenameofchoice.jpg')



.. image:: _static/video_out.jpg
