from collections import defaultdict
from queue import PriorityQueue

import sys

def initialize_graph():
    V, E = [int(x) for x in input().split()]
    graph = defaultdict(list)

    for i in range(E):
        a, b = [int(x) for x in input().split()]
        graph[a].append([b, 0])
        graph[b].append([a, 0])
    return graph

def prim(graph):
    visited = [False] * len(graph.keys())
    visited[0] = True

    q = PriorityQueue()
    q.put((0, 0, -1))

    MST = []
    while not q.empty():
        key, node, parent = q.get()
        visited[node] = True

        if parent != -1:
            MST.append([parent, node, key])

        for neighbour in graph[node]:
            if not visited[neighbour[0]]:
                q.put((neighbour[1], neighbour[0], node))
    return MST

def main():
    graph = initialize_graph()

if __name__ == "__main__":
    main()