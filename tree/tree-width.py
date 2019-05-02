from queue import Queue

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def width(root : Node):
    if root is None:
        return 0
         
    q = Queue()
    max_width = 0
    q.put((root, 0))

    while not q.empty():
        count = len(q)

        left, right = float('inf'), -float('inf')
        for i in range(count):
            node, idx = q.get()
            left = min(left, idx)
            right = max(right, idx)

            if node.left is not None:
                q.put((node.left, 2*idx + 1))


            if node.right is not None:
                q.put((node.right, 2*idx + 2))
        max_width = max(max_width, right - left + 1)
    return max_width

