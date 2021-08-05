
Image color recognition
=======================

Example 1
---------

As a walk through some of the capabilities of ColorDetect we will use
this sample image.

.. image:: _static/doc_image.jpg

::

    # Get the most dominant color count from an image
    >>> from colordetect import ColorDetect
    >>>
    >>> my_image = ColorDetect("<image_path>")
    >>> my_image.get_color_count(color_format="rgb")
    '[2.0, 2.0, 249.0]': 6.2, '[5.0, 211.0, 212.0]': 7.15, '[173.0, 25.0, 98.0]': 17.49, '[146.0, 155.0, 9.0]': 18.62, '[253.0, 253.0, 253.0]': 50.54}

A dictionary, with the RGB value of the color as the key and its percentage occurrence in the image
as the value is returned.
To get a more human readable format, one would call ``get_color_count()`` parsing the parameter
for ``color_format`` as **human_readable**.

Our line to obtain colors would be replaced by::

    >>> my_image.get_color_count()
    {'blue': 6.2, 'darkturquoise': 7.15, 'mediumvioletred': 17.49, 'olive': 18.62, 'white': 50.54}


.. note:: As of the ColorDetect 0.1.7, the percentage changed from being presented as a
          key to being presented as a value. This attributed to the uniqueness of python
          dictionary keys. See the :ref:`change log<0.1.7>` for more info.


For clarification::

    '[2.0, 2.0, 249.0]': 6.2
    # this key value pair would imply 6.2 % of the image, has an RGB of [2.0, 2.0, 249.0]



By default, `ColorDetect <https://colordetect.readthedocs.io/en/latest/>`_ will count
the 5 most dominant colors. This can , of course ,be overridden by parsing an argument specifying how many
colors most dominant you need from the image, with values decreasing in their percentage presence
the higher you go on the color count.

Look up :ref:`get_color_count<get_color_count>` for details
on the different arguments it accepts including the different color format return values.
Now suppose you want to take it a step further and write the result to the image itself.

.. warning:: Take note of the difference in saving the image to storage from the previous
             `save_color_count<save_color_count>` to `save_image<save_image>`

::


    >>> my_image.write_color_count()
    >>> my_image.save_image("<path_to_save_image>", "<name_of_image>")

Just as `save_color_count`,  :ref:`save_image<save_color_count>` will accept , as optional parameters, the path and name of the image with color count on it.
By default, these values are ``.`` (For the current directory the script is being run from)
and ``out.jpg`` respectively.

The result.

.. image:: _static/out_rgb.jpg


Depending on the size of the image, you might want to decide whether
to write the count to the image or not. As observed, a smaller image gives
a crowded appearance.

As a similar example, with colors represented in their hex format,

.. image:: _static/out_hex.jpg


Additionally, to enable the use of custom text on an image:

::

    >>> from colordetect import ColorDetect
    >>> my_image = ColorDetect("<image_path>")
    >>> my_image.write_text(text="a random string", font_color=(0,0,0))


.. image:: _static/out_random_string.jpg

To appropriately place the text onto the image and ensure the text does not fade over the object
on the image with the same color, a font color can be parsed as an RGB tuple. This defaults to
`(0,0,0)` , which would be black.
More customization features over the text, including text margin, font thickness and line
spacing (the space between lines of text) can be found on the :ref:`write_text<module_ColorDetect>`
method documentation.

Whether using ``write_text`` or ``write_color_count``, the image has to be saved using `save_image`.


Getting colors from URL:
------------------------


::

    >>> from colordetect import ColorDetect
    >>>
    >>> my_image = ColorDetect("<image_url>")
    >>> my_image.get_color_count()


Example 2
---------

We get colors from a random image on unsplash.

Our photo of choice, is one by  `Ruby Cevallos <https://unsplash.com/@rubylordez?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText/>`_ on `Unsplash <https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText/>`_ 
  

::

    >>> from colordetect import ColorDetect
    >>>
    >>> my_image = ColorDetect("https://images.unsplash.com/photo-1628127437106-0cc010a5fd2d?ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60")
    >>> my_image.get_color_count()
    {'saddlebrown': 6.17, 'sienna': 12.62, 'rosybrown': 15.62, 'lightgray': 27.67, 'whitesmoke': 37.91}

    We may, go ahead and write this color count to the image, and save it.



Video color recognition can be done using :ref:`VideoColor<video_color_recognition>`