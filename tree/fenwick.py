import sys 

class Fenwick():
    def __init__(self, n):
        self.tree = [0] * (n+1)
        self.size = n
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index = index + (index & -index)
    
    def get_sum(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index = index - (index & -index)
        return sum
    
    def build_tree(self, arr):
        for i in range(1, len(arr)+1):
            self.update(i, arr[i-1])

if __name__ == "__main__":
    arr = list(range(1, 9))
    BIT = Fenwick(len(arr))
    BIT.build_tree(arr)
    print(BIT.tree)