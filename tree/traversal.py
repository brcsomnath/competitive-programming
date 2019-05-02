import queue

class Node():
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

def min_depth(root):
    if root is None:
        return 0

    # Level order traversal

    q = queue.Queue()
    q.put({'node': root, 'depth': 1})

    while not q.empty():
        item = q.get()
        node = item['node']
        depth = item['depth']

        if node.left is None and node.right is None:
            return depth
        
        if node.left is not None:
            q.put({'node': node.left, 'depth': (depth+1)})
        
        if node.right is not None:
            q.put({'node': node.right, 'depth': (depth+1)})

def level_order_traversal(root):
    q = queue.Queue()
    q.put(root.value)

    while not q.empty():
        node = q.get()
        print(node.value)

        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)

def level_order_traversal_spiral(root):
    q = queue.Queue()
    q.put(root.value)

    while not q.empty():
        

def main():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    print(min_depth(root))
    


if __name__ == "__main__":
    main()    