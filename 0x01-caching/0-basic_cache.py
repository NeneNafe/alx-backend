#!/usr/bin/env python3
"""a class BasicCache that inherits from BaseCaching and
is a caching system"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """A method in the inherited class"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None:
            return None

        return self.cache_data.get(key)
