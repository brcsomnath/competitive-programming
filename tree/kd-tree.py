
class Node()
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class KDTree():
    def __init__(self):
        self.root = None
        self.N = 0
    
    def update(self, node, parent):
        if node is None:
            node = Node(val)
        else:
            parent = node

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.N = len(self.root.data)
        
        count = 0
        ndoe = self.root
        while node is not None:
            idx = count & 1

            if val < node.data[idx]:
                self.update(node.left, node)
            else:
                self.update(node.right, node)

            count += 1
