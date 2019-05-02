from collections import deque

class LRUCache():
    def __init__(self, N):
        self.capacity = N
        self.lru = deque()
        self.cache = dict()
        self.time = 0

    def refer(self, key):
        if key not in self.cache.keys():
            if len(self.lru) == self.capacity:
                self.element = self.lru.popleft()
                del self.cache[self.element]
        else:
            
