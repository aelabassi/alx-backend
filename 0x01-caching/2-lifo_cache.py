#!/usr/bin/env python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache class """
    def __init__(self):
        """ Override superclass __init__ """
        super().__init__()

    def put(self, key, item):
        """ Add key/value pair to cache data """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = sorted(self.cache_data.keys())[-2]
            print("DISCARD: {}".format(last))
            del self.cache_data[last]

    def get(self, key):
        """ Retrieve value from cache data """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
