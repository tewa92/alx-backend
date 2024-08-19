#!/usr/bin/env python3
""" Simple helper function """
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Returns a tuple of size two containing a start index and an end index
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "7d3576d97e7560ae85135cc214ffe2b3412c51d7.xls"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start:end]
