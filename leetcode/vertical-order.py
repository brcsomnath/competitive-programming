'''
314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values.
 (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
'''

from collections import defaultdict

class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

def util(node, skew, skew_dict):
    skew_dict[skew] = node.data

    if node.left is not None:
        util(node.left, skew - 1, skew_dict)
    
    if node.right is not None:
        util(node.right, skew + 1, skew_dict)
        
def process(root):
    skew_dict = defaultdict(list)
    util(root, 0, skew_dict)

def main():
    pass

if __name__ == "__main__":
    main()