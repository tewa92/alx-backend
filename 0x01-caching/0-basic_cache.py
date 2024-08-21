#!/usr/bin/env python3
'''
BasicCache class that inherits from BaseCaching and is a caching system
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching
    """

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
