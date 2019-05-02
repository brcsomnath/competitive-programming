def make_set(node, parent, size):
    parent[node] = node
    size[node] = 1

def find_set(node, parent):
    if parent[node] == node:
        return node
    return parent[node] = find_set(parent[node])

def main():
    N = int(input())
    queries = []
    while True:
        x = input()
        if len(x) <= 0:
            break
        queries.append([int(num) for num in input().split()])
    
    answers = [0] * N
    parent = [-1] *  N
    size = [0] * N

    for i in range(N):
        make_set(i)

    for i in range(N-1, -1, -1):
        l, r, c = queries[i]

        idx = find_set(l)
        while idx <= r:
            answers[idx] = c
            parent[idx] = idx + 1
            idx = parent[idx]

    return answers

if __name__ == "__main__":
    main()


# By rank and path compression with path length storage

def make_sets(node, parent, rank):
    parent[node] = [node, 1]
    rank[node] = node

def find_sets(node, parent, rank):
    if node != parent[node][0]:
        dist = parent[node][1]
        parent[node] = find_sets(parent[node][0], parent, rank)
        parent[node][1] += dist
    return parent[node]

def union_sets(node1, node2, parent, rank):
    par1 = find_sets(node1, parent, rank)
    par2 = find_sets(node2, parent, rank)

    if par1 != par2:
        if rank[node1] < rank[node2]:
            node1, node2 = node2, node1
        parent[node2] = [par1, 1]
        if rank[node1] == rank[node2]:
            rank[node1] += 1