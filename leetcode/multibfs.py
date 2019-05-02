'''
A multiple-source BFS works in exactly the same way as regular BFS,
but instead of starting with a single node, you would put all your sources (A's)
in the queue at the beginning. That is, make a pass over the grid to find all A's
and initialize your BFS queue with all of them at distance 0. Then proceed with BFS as normal.

Here's an example Python implementation:
'''

from collections import deque
from itertools import product

def get_distance():
    grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', 'A', 'A', 'A', '0', '0', '0', '0', '0'],
            ['0', 'A', 'A', '0', '0', '0', '0', '0', '0'],
            ['0', 'A', 'A', 'A', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', 'B', '0', '0'],
            ['0', '0', '0', '0', '0', 'B', 'B', 'B', '0'],
            ['0', '0', '0', '0', '0', 'B', 'B', 'B', 'B']]
    R = C = 9  # dimensions of the grid
    queue = deque()
    visited = [[False]*C for _ in range(R)]
    distance = [[None]*C for _ in range(R)]
    for row, col in product(range(R), range(C)):
        if grid[row][col] == 'A':
            queue.append((row, col))
            distance[row][col] = 0
            visited[row][col] = True
    while queue:
        r, c = queue.popleft()
        for row, col in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)):  # all directions
            if 0 <= row < R and 0 <= col < C and not visited[row][col]:
                distance[row][col] = distance[r][c] + 1
                if grid[row][col] == 'B':
                    return distance[row][col]
                visited[row][col] = True
                queue.append((row, col))    

print(get_distance())  # 6