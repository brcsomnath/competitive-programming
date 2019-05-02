
def floyd_warshall(graph):
    V = len(graph)

    dist = [[float('inf') for i in range(V)] for j in range(V)]

    for u in range(len(graph.keys())):
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for i in range(V):
        for j in range(V):
            for k in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

'''
Detecting negative cycles
For self loops, if the distance to itself
is negative, then negative cycles exist
'''

def detect_negative_cycle(graph):
    dist = floyd_warshall(graph)

    for i in range(len(graph)):
        if dist[i][i] < 0:
            return True
    return False

'''
Applications of FW Algorithms
Find the diameter of a graph which is the maximal shortest path

# General Tips
For large undirected graphs V, E ~ 10M, use BFS
Directed graphs, use Dijkstra
Negative weights, Bellman Ford
Very small graphs, V<400, use FW algo
'''

# For minimax distance
def minmax(graph):
    V = len(graph.keys())
    dist [[float('inf') for i in range(V)] for j in range(V)]

    for u in len(graph.keys()):
        for next in graph[u]:
            neighbour, weight = next
            dist[u][neighbour] = weight

    for i in range(V):
        for j in range(V):
            for k in range(V):
                dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))
