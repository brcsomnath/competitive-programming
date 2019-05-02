from collections import defaultdict

graph = defaultdict(list)

def transpose_graph(graph):
    inv_graph = defaultdict(list)

    for vertex in graph.keys():
        for neighbour in graph[vertex]:
            inv_graph[neighbour].append(vertex)

    return inv_graph

def dfs(graph, src, visited, stack):
    visited[src] = True

    for neighbour in graph[src]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited)
    stack.append(src)

def SCC_dfs(graph, src, visited, conn):
    visited[src] = True
    conn.append(src)

    for neighbour in graph[src]:
        if not visited[neighbour]:
            SCC_dfs(graph, neighbour, visited, conn)

def find_SCC(graph):
    stack = []
    visited [False]*len(graph.keys())

    for v in graph.keys():
        if not visited[v]:
            dfs(graph, v, visited, stack)
    
    inv_graph = transpose_graph(graph)
    visited = [False] * len(graph.keys())

    scc = []
    while len(stack) > 0:
        v = stack.pop()
        conn = []

        if not visited[v]:
            SCC_dfs(graph, v, visited, conn)
        scc.append(conn)
    return scc


