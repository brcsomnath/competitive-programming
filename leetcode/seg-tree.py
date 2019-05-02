import sys 

class Node():
    def __init__(self, data):
        self.max = data
        self.min = data

class SegTree():
    def __init__(self, n):
        self.tree = [Node(-1)]* (2*n)
    
    def form_node(self, index):
        self.tree[index].max = max(self.tree[index<<1].max, self.tree[index<<1 | 1].max)
        self.tree[index].min = min(self.tree[index<<1].min, self.tree[index<<1 | 1].min)
    
    def build(self, arr):
        n = len(arr)
        for i in range(len(arr)):
            self.tree[n + i] = Node(arr[i])
        
        for i in range(len(arr)-1, -1, -1):
            self.form_node(i)
            print("[" + str(self.tree[i].min) + ", " + str(self.tree[i].max) + "]")

    def print_tree(self):
        for i in range(len(self.tree)):
            print("[" + str(self.tree[i].min) + ", " + str(self.tree[i].max) + "]")
    
    def query(self, start, end, left, right):
        pass 

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    st = SegTree(len(x))
    st.build(x)
    # st.print_tree()