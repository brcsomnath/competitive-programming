
from collections import deque

def make_set(parent, rank, node):
    parent[node] = node
    rank[node] = 0

def find_parent(parent, node): # recursive
    if parent[node] == node:
        return node
    return parent[node] = find_parent(parent, parent[node])

def find_parent(parent, node): # iterative
    while parent[node] != node:
        node = parent[node]
        parent[node] = parent[parent[node]] # Path compression
    return node


def union(x, y, parent, rank):
    x1 = find_parent(parent, x)
    y1 = find_parent(parent, y)

    if x1 != y1:
        if rank[x1] < rank[y1]:
            parent[x1] = y1
        elif rank[x1] > rank[y1]:
            parent[y1] = x1
        else:
            parent[y1] = x1
            rank[y1] += 1

def krushkal(graph, V):
    edges = deque(sorted(graph, key = lambda item : item[2]))

    count = 0
    MST = []

    parent = dict()
    rank = dict()

    for i in range(V):
        make_set(parent, rank, i)

    while count < V:
        edge = edges.popleft()

        u, v, w = edge
        x = find_parent(u)
        y = find_parent(v)

        if x != y:
            count += 1
            MST.append([u, v, w])
            union(x, y, parent, rank)

    return MST