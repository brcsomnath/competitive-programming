'''
298. Binary Tree Longest Consecutive Sequence
Question
 Solution

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree
along the parent-child connections. The longest consecutive path need to be from parent to 
child (cannot be the reverse).
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

max_len = 0

def recursive_call(node, root, length):
    if node != None:
        if node.value == (root.value + 1):
            max_len = max(max_len, length + 1)
            process(node, 1)
        else:
            max_len = max(max_len, length + 1)

def process(root, length):
    if root == None:
        return 0

    recursive_call(root.left, root, length)
    recursive_call(root.right, root, length)

def main():

if __name__ == "__main__":
    main()