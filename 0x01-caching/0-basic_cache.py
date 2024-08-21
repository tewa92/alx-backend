#!/usr/bin/env python3
''' BasicCache class that inherits from BaseCaching and is a caching system '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            first_item = keys[0]
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
