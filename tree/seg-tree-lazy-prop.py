
N = 100
tree = [0] * (2*N)
d = [0] * N

def combine(x, y):
    return x + y

def apply(pos, value):
    tree[pos] += value
    if pos < N:
        d[pos] += value

def build(pos): # called when update occurs to update parents
    while pos > 1:
        pos >>= 1
        tree[pos] = combine(tree[pos>>1], tree[pos>>1|1]) + d[pos]

def push(pos):
    for height in range(h, 0, -1):
        x = pos >> height
        if d[x] != 0:
            apply(x<<1, d[x])
            apply(x<<1|1, d[x])
            d[x] = 0

# Inclusive range (left, right)
def update(left, right, value):
    left += N
    right += N
    l, r = left, right

    while left < right:
        if left & 1:    apply(left, value)  # lazy propagation
        if right & 1 == 0:   apply(right, value) # lazy propagation
        left, right =  (left + 1)>>1, (right - 1)>>1
    build(l)
    build(r)

def query(left, right):
    left += N
    right += N

    push(left)
    push(right)
    res = 0

    while left < right:
        if left & 1:    res = combine(res, tree[left])
        if right & 1 == 0:  res = combine(res, tree[right])
        left, right = (left + 1)>>1, (right - 1)>>1
    return res
    