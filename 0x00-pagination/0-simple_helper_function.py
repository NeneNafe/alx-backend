#!/usr/bin/env python3
"""This is a function named index_range that takes two integer
arguments page and page_size"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start
index and an end index

    Args:
        page (int): The page number
        page_size (int): The number of items per page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
