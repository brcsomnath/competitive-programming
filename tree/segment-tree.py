tree = [0]*(2*N)

def combine(x, y):
    return x + y 

def build_tree(tree, N):
    for i in range(n-1, 0, -1):
        tree[i] = combine(tree[i<<1], tree[i<<1|1])

def modify_interval(left, right, val):
    left += N 
    right += N 

    while left < right:
        if left & 1:
            tree[left] += val
            left += 1

        if right & 1:
            tree[right] += val
            right -= 1
        left, right = left << 1, right << 1
    
def modify(pos, val, N):
    pos += N
    tree[pos] = val
    while pos > 0:
        tree[pos>>1] = combine(tree[pos], tree[pos^1])
        pos >>= 1

def query(left, right):
    left += N 
    right += N 

    res = 0

    while left < right:
        if left & 1: # right child, left is included so skip parent and move to the right
            res += combine(res, tree[left])
            left += 1
        
        if right & 1: # same logic
            res += combine(res, tree[right])
            right -= 1
        left , right = left >> 1, right >> 1
    return res

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    N = len(arr)
    for i in range(N):
        tree[i+N] = arr[i]
    build_tree(tree, N)
