from queue import PriorityQueue

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