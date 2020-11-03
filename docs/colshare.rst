.. _col_share:
col_share
=========
Depending on how many colors you have or how many dominant colors you want to narrow down to:

::

    >>> from colordetect import col_share
    >>> all_colors = my_video.get_video_frames()
    >>> top_colors = col_share.sort_order(object_description=all_colors,key_count=5)
    {'[0.0, 0.0, 0.0]': 68.83, '[5.0, 7.0, 24.0]': 22.48, '[5.0, 8.0, 24.0]': 22.22, '[4.0, 7.0, 24.0]': 21.7, '[6.0, 9.0, 26.0]': 19.11}

The sort gets the top 5 colors, by default, from all the colors obtained from all the frames present. This may be adjusted to suit your needs.
A reverse of the same may be obtained by passing the  `ascending` parameter and setting this to false: ``ascending=False``.

::

    >>> top_colors = col_share.sort_order(object_description=all_colors,key_count=5, ascending=False)
