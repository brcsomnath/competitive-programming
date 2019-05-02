'''
251. Flatten 2D Vector

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements 
returned by next should be: [1,2,3,4,5,6].
'''

class Interator():
    def __init__(self, vec):
        self.arr = []
        for x in vec:
            self.arr.append(x)
        self.N = len(self.arr)
        self.count = 0
    
    def has_next(self):
        return self.count <= self.N
    
    def next(self):
        self.count += 1
        return self.arr[self.count - 1]

