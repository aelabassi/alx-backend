#!/usr/bin/env python3
""" LRU caching """
from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRU caching """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ LRU cache """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                discarded, _ = self.cache_data.popitem(True)
                print("DISCARD: {:s}".format(discarded))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
