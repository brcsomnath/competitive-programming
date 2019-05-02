from collections import *
from queue import Queue
import sys

def dfs(graph, src, parent, visited):
    visited[src] = True

    for v in range(len(graph[src])):
        if not visited[v] and graph[src][v] > 0:
            parent[v] = src
            dfs(graph, v, parent, visited)
            
def dfs_util(graph, src, tank, parent):
    visited = [False] * len(graph)
    dfs(graph, src, parent, visited)
    return visited[tank]

'''
Edmond Karp version of FF algo
'''
def bfs(graph, src, tank, parent):
    visited = [False] * len(graph)

    visited[src] = True
    q = Queue()
    q.put(src)

    while not q.empty():
        u = q.pop()
        for v in range(len(graph[u])):
            if not visited[v] and graph[u][v] > 0 :
                parent[v] = u
                q.put(v)
    return visited[tank]

'''
For multi-source and multi-sink problems
Create a super source (ss) and super tank (st)
Connect all sources with ss with infinite capacity
And all tanks with st with infinite capacity
'''
def ford_fulkerson(graph, src, tank):
    max_flow = 0
    parent = dict()

    residual_graph = graph

    while bfs(residual_graph, src, tank, parent): 
        # find valid flow path till there's none left
        min_path_flow = float('inf')
        start, end = tank, src
        while start != end:
            v = parent[start]
            min_path_flow = min(min_path_flow, residual_graph[v][start])
            start = v

        start, end = tank, end
        while start != end:
            v = parent[start]
            residual_graph[v][start] -= min_path_flow
            residual_graph[start][v] += min_path_flow
            start = v

        max_flow += min_path_flow
    return max_flow, residual_graph

def min_cut(graph, src, tank):
    _, residual_graph = ford_fulkerson(graph, src, tank)

    visited = [False] * len(graph)
    dfs(residual_graph, src, [-1]*len(graph), visited)

    min_cuts = []

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if visited[i] and not visited[j] and graph[i][j] > 0:
                min_cuts.append([i, j])
    return min_cuts