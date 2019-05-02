
from queue import Queue

class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def max_width(root):
    q = Queue()
    q.put(root)

    max_width = 0

    while not q.empty():
        width = len(q)
        max_width = max(max_width, width)

        for i in range(width):
            node = q.get()

            if node.left is not None:
                q.put(node.left)
            
            if node.right is not None:
                q.put(node.right)
    return max_width