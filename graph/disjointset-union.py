from collections import defaultdict

parent = defaultdict(lambda: -1)

# This takes O(n) time complexity, with long chains
def find_parent(node):
    if parent[node] == -1 or parent[node] == node:
        return node
    return find_parent(parent[node])

def union(src, dest):
    src_parent = find_parent(src)
    dest_parent = find_parent(dest)
    if src_parent != dest_parent:
        parent[src_parent] = dest_parent

def union_find(pairs):
    for pair in pairs:
        src, dest = pair
        union(src, dest)

def process(words1, words2, pairs):
    if len(words1) != len(words2):
        return False

    union_find(pairs)
    print(parent)
    for i in range(len(words1)):
        if find_parent(words1[i]) != find_parent(words2[i]):
            return False
    return True