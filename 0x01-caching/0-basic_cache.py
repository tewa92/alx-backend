#!/usr/bin/python3
import base_caching


class BasicCache(base_caching.BaseCaching):
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
