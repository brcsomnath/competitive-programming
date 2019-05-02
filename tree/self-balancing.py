'''
Util rotate functions for Splay and AVL trees
'''

def Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def right_rotate(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root

def left_rotate(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root
