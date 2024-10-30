#!/usr/bin/env python3
""" FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print("DISCARD: {}".format(first))
                del self.cache_data[first]

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
