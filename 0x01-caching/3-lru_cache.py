#!/usr/bin/env python3
"""a class LRUCache that inherits from BaseCaching and is
a caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A class that inherits from BaseCaching and
    a caching system"""
    def __init__(self):
        """Initializes the init function"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
