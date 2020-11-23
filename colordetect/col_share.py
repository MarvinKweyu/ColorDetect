"""
.. _module_colShare
Module ColShare
===============
Global methods non-object specific

Usage:


>>> from colordetect import col_share
# show a progress bar for a process
>>> col_share.progress_bar("<current_process_position>", "<total_process_length>", "<process_description>")
# sort a dictionary by value to required length or in specific order
>>> col_share.sort_order('<dictionary>', "<items_to_return>", "<order>")
"""

import sys


def progress_bar(position: int, total_length: int, post_text: str = "Color Detection"):
    """
    progress_bar
    ----------------
    Display a progress bar of video processing

    Parameters
    ----------
    position: int
        Current position of process
    total_length: int
        Total length of process
    post_text: str
        Text to display along with progress bar
    """
    n_bar = 100
    #       # size of progress bar
    j = position / total_length
    sys.stdout.write("\r")
    sys.stdout.write(f"[{'#' * int(n_bar * j):{n_bar}s}] {int(100 *j)}% {post_text}")
    sys.stdout.flush()


def sort_order(object_description: dict, key_count: int = 5, ascending: bool = True):
    """
    .. _color_sort
    sort_order
    ----------------
    Sort items in a dictionary according to value

    Parameters
    ----------
    object_description: dict
        A dictionary whose values need sorting
    key_count: int
        The number of items to return from the sort
    ascending: bool
        The order to perform the dictionary sort. By default, set to True.
    :return: A sorted dictionary with specific number
    """
    if type(key_count) != int:
        raise TypeError(
            f"color_count has to be an integer. Provided {type(key_count)} "
        )

    if type(ascending) != bool:
        raise TypeError(
            f"The value of the 'ascending' parameter is a boolean. Provided {type(ascending)} "
        )

    sorted_colors = {
        k: v
        for k, v in sorted(
            object_description.items(), key=lambda item: item[1], reverse=ascending
        )
    }
    return dict(list(sorted_colors.items())[0:key_count])
