#!/usr/bin/env python3
""" LRU caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ LRU cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = sorted(self.cache_data.keys(), reverse=True)
            print("DISCARD: {}".format(last[-2]))
            del self.cache_data[last[-2]]

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data[key] = self.cache_data.pop(key)
        return self.cache_data[key]
