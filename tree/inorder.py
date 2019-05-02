
class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def inorder(root):
    stack = []

    node = root
    ans = []

    while node is not None or len(stack) > 0:
        if node is not None:
            stack.append(node)
            node = node.left
            continue
        
        node = stack.pop()
        ans.append(node.data)
        node = node.right

    return ans
