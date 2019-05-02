'''
379. Design Phone Directory

Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
'''
from collections import *

class PhoneDirectory():
    def __init__(self):
        self.N = 0
        self.q = deque()
        self.empty_slot = defaultdict(lambda: 0)

    def get(self):
        if len(self.q) == 0:
            self.N += 1
            return self.N
        
        n = self.q.popleft()
        self.empty_slot[n] -= 1
        return n
    
    def release(self, slot):
        if self.empty_slot[slot] == 0:
            self.empty_slot[slot] += 1
            self.q.append(slot)
    
    def check(self, slot):
        return self.empty_slot[slot] > 0

    
