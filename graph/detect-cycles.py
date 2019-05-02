from collections import defaultdict

graph = defaultdict(list)

def dfs(graph, src, visited, parent):
    visited[src] = True
    for neighbour in graph[src]:
        if visited[neighbour] and parent != neighbour:
            return True
        
        if dfs(graph, neighbour, visited, src):
            return True
    return False


def main():
    while True:
        inp = input()
        if len(input()) == 0:
            break
        x, y = inp
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * len(graph.keys())


if __name__ == "__main__":
    main()