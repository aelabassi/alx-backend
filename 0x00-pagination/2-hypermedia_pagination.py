#!/usr/bin/env python3
""" Hypermedia pagination """
import csv
import math
from typing import Dict, Any, List
index_page = __import__('0-simple_helper_function').index_range


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
        """ Get page
        Args:
            page: int
            page_size: int
        Return:
            List[List]
            """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_page(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ Get hypermedia pagination
        Args:
            page: int
            page_size: int
        Return:
            Dict[str, Any]
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        data = self.dataset()
        total = len(data)
        start, end = index_page(page, page_size)
        data = data[start:end]
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if end < total else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": math.ceil(total / page_size)
        }
