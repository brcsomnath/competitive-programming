'''
369. Plus One Linked List

Given a non-negative integer represented as non-empty a singly
linked list of digits, plus one to the integer. You may assume the integer
do not contain any leading zero, except the number 0 itself. The digits are 
stored such that the most significant digit is at the head of the list.
'''

class Node():
    def __init__(self, val):
        self.data = val
        self.next = None
    
def process(root, node):
    if node.next == None:
        node.val = (node.val + 1)%10
    else:
        node.val = (node.val + process(root, node.next))%10
    return 1 if node.val == 0 else 0
    
def main():
    root = Node(4)
    process(root, root)

    if root.val == 10:
        root.val = 0
        new_root = Node(1)
        new_root.next = root
        root = new_root

if __name__ == "__main__":
    main()
