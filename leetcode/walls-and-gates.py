'''
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent 
INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach 
a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''

from queue import Queue
from collections import defaultdict

INF = 2147483647


def multi_source_bfs(matrix, sources):
    q = Queue()

    for src in sources:
        q.put(src)
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = defaultdict(lambda : False)

    while not q.empty():
        row, col = q.get()
        visited[(row, col)] = True
        for d in directions:
            r, c = row + d[0], col + d[1]
            if matrix[r][c] == INF and not visited[(r, c)]:
                matrix[r][c] = matrix[row][col] + 1
                q.put([r, c])

def process(matrix):
    sources = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                sources.append([r, c])
    multi_source_bfs(matrix, sources)
    return matrix
    
