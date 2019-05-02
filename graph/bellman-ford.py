

def bellman_ford(graph, source):
    distance, predecessor = dict(), dict()

    for v in graph.keys():
        distance[v], predecessor[v] = float('inf'), None
    distance[source] = 0
    
    # A shortest path can have at most (V-1) edges 
    for _ in range(len(graph.keys())-1):
        # relax E edges V-1 times
        for v in graph.keys():
            for next in graph[v]:
                neighbour, weight = next
                if distance[v] != float('inf') and distance[neighbour] > weight + distance[v]:
                    distance[neighbour], predecessor[neighbour] = weight + distance[v], v # relax


    for v in graph.keys():
        for next in graph[v]:
            neighbour, weight = next
            if distance[neighbour] > distance[v] + weight:
                return True