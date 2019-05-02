import queue
import sys
from collections import defaultdict
from queue import PriorityQueue

def initialize_graph():
    V, E = [int(x) for x in input().split()]
    graph = defaultdict(list)

    for i in range(E):
        a, b = [int(x) for x in input().split()]
        graph[a].append([b, 0])
        graph[b].append([a, 0])
    return graph

def BFS(graph, start):
    q = queue.Queue(maxsize= len(graph))
    q.put(start)

    visited = [False]* (len(graph))
    visited[start-1] = True

    while not q.empty():
        s = q.get()
        print('Next element : ', s)

        for x in graph[s]:
            if not visited[x[0]-1]:
                visited[x[0]-1] = True
                q.put(x[0])

def DFS(graph, start, visited):
    visited[start - 1] = True

    print('Next Element: ', start)

    for x in graph[start]:
        if not visited[x[0] - 1]:
            visited[x[0]-1] = True
            DFS(graph, x[0], visited)

def check_bipartite(graph):
    start = 1

    q = queue.Queue(maxsize=len(graph))
    q.put(start)

    colors = [-1]*len(graph)
    color[start] = 1

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if colors[v[0]] == colors[u]:
                return False
            
            if colors[v[0]] == -1:
                colors[v[0]] = 1 - colors[u]
                q.put(v[0])
    return True

def find_min(dist, visited):
    min_ = sys.maxsize
    idx = -1

    for i in range(len(dist)):
        if dist[i] < min_ and not visited[i]:
            min_ = dist[i]
            idx = i
    return idx

def dijkstra(graph, start):
    visited = [False] * (len(graph))
    dist = [sys.maxsize] * (len(graph))

    dist[start] = 0

    for i in range(len(graph) - 1):
        u = find_min(dist, visited)
        visited[u] = True

        for v in graph[u]:
            if not visited[v[0]] and dist[u] != sys.maxsize and dist[u] + v[1] < dist[v[0]]:
                dist[v[0]] = dist[u] + v[1]

def dijkstra_queue(graph, src):
    visited = [False]*len(graph.keys())
    dist = [float('inf')]*len(graph.keys())

    pq = PriorityQueue()
    pq.put((0, src))]
    dist[src] = 0

    while not pq.empty():
        weight, vertex = pq.pop()
        visited[vertex] = True

        for neighbour in graph[vertex]:
            if not visited[neighbour] and dist[neighbour] > dist[vertex] + weight:
                dist[neighbour] = dist[vertex] + weight
                pq.put((dist[neighbour], neighbour))

def main():
    graph = initialize_graph()
    BFS(graph, 2)

    visited = [False]*(len(graph))
    DFS(graph, 2, visited)
    


if __name__ == '__main__':
    main()