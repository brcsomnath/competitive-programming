'''
Dinic Algorithm for max flow
O(EV^2) over Edmond Karp O(VE^2)
'''

from collections import defaultdict
from queue import Queue

graph = defaultdict(list)

class Edge():
    def __init__(self, dest, weight, src):
        self.V = dest
        self.capacity = weight
        self.flow = 0
        self.reverse = src # quickly get the other edge

'''
Adding an edge to the graph
'''
def add_edge(src, dest, weight):
    forward_edge = Edge(dest, weight, len(graph[src]))
    backward_edge = Edge(src, 0, len(graph[dest]))
    graph[src].append(forward_edge)
    graph[dest].append(backward_edge)

'''
BFS to check if tank is reachable from source
If there exists a positive path
'''
def bfs(src, tank):
    V = len(graph.keys())
    level = [-1] * V

    level[src] = 0
    q = Queue()
    q.put(src)
    
    while not q.empty():
        u = q.pop()
        for edge in graph[u]:
            if level[edge.V] == -1 and (0 < edge.flow <= edge.capacity):
                level[edge.V] = level[u] + 1
                q.put(edge.V)

    return level[tank] >= 0

def send_flow(flow, src, dest):
    if src == dest:
        return flow

    for edge in graph[src]:
        curr_flow = min(flow, edge.flow)
        future_flow = send_flow(curr_flow, edge.dest, dest)

        if future_flow > 0:
            edge.flow += future_flow
            graph[edge.V][edge.reverse] -= future_flow
            return future_flow
    return 0

def dinic(source, tank):
    max_flow = 0
    while bfs(source, tank):
        max_flow += send_flow(float('inf'), source, tank)
    return max_flow

