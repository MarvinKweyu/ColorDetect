Welcome to ColorDetect's documentation
======================================

This site covers ColorDetect's usage and method documentation.

Getting started
===============

Installation
------------
From pypy::

    pip install ColorDetect

For usage , import as::

    import ColorDetect



Examples
========

As a walk through some of the capabilities of ColorDetect we will use
this sample image.

.. image:: _static/doc_image.jpg

::

    # Get the most dominant color count from an image
    >>> import ColorDetect
    >>>
    >>> my_image = ColorDetect("<image_path>")
    >>> my_image.get_color_count()
    {6.2: array([  2.008,   2.07 , 249.287]), 7.15: array([  5.083, 210.89 , 212.356]), 15.71: array([172.708, 167.685,   5.291]), 20.41: array([148.619,  33.651,  88.661]), 50.53: array([253.272, 253.382, 252.612])}

A dictionary, with the RGB value of the color as the key and its percentage occurrence in the image
as the value is returned.

Now suppose you want to take it a step further and write the result to the image itself.

::

    my_image.save_color_count("<path_to_save_image>", "<name_of_image>")

The ``save_color_count`` method will accept , as optional parameters, the path and name of the image with color count on it.
By default, these values are ``.`` (For the current directory the script is being run from)
and ``out.jpg`` respectively.

The result.

.. image:: _static/out.jpg


Depending on the size of the image, you might want to decide whether
to write the count to the image or not. As observed, a smaller image gives
a crowded appearance.


Developer Notes
===============

Here, we dive into ColorDetect's inner definitions and working.
Found a bug or feature request you would like to address? Take a look at the  `Contribution guidelines <https://github.com/MarvinKweyu/ColorDetect/blob/master/CONTRIBUTING.md>`_
and feel free to submit a pull. The project source is hosted on `Github <https://github.com/MarvinKweyu/ColorDetect/>`_

.. automodule:: colordetect.color_detect
   :members:
   :undoc-members:
   :show-inheritance:


.. automodule:: colordetect
   :members:
   :undoc-members:
   :show-inheritance:

