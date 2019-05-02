'''
Given an input stream of boolean values, design a data structure that can support 
following modules in optimal time-

i) setTrue(index)
ii) setFalse(index)
iii) setAllTrue()
iv) setAllFalse()
v) getIndex(index)
'''

tree = [-2] * (2*N)
diff = dict()

def combine(x, y):
    if x == y:
        return x
    return -1

def build_tree():
    for i in range(N-1, 0, -1):
        tree[i] = combine(tree[i<<1], tree[i<<1|1])
    
def get_index(index):
    return tree[index + N] == 1

def push():
    if tree[1] == -1:
        return 
    
    for i in range(2, 2*N):
        tree[i] = tree[1]

def set_all_true():
    tree[1] = 1

def set_all_false():
    tree[1] = 0

def set_true(index):
    index += N
    tree[index] = 1

    diff[index] = 1

def set_false(index):
    index += N
    tree[index] = 0

    diff[index] = 0

if __name__ == "__main__":
    arr = list(map(bool, input().split()))
    for i in range(N):
        tree[N+i] = 1 if arr[i] else 0


