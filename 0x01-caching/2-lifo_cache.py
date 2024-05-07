#!/usr/bin/env python3
""" a class LIFOCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initializes the init function"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        return self.cache_data.get(key)
