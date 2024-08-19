#!/usr/bin/env python3
""" Simple helper function """
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    Returns a tuple of size two containing a start index and an end index
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

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
        """ Get the page of the dataset"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Get the page of the dataset"""
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": None if page >= total_pages else page + 1,
            "prev_page": None if page <= 1 else page - 1,
            "total_pages": total_pages
        }
        return page_info
