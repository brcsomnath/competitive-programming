'''
The Maze II

There is a ball in a maze with empty spaces and walls. The ball can go through 
empty spaces by rolling up, down, left or right, but it won't stop rolling until 
hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest
 distance for the ball to stop at the destination. The distance is defined by the 
 number of empty spaces traveled by the ball from the start position (excluded) to
  the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty
 space. You may assume that the borders of the maze are all walls. The start and 
 destination coordinates are represented by row and column indexes.
'''

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(src, dest, maze, cost, visited):
    visited[src] = True
    if src == dest:
        return cost

    for d in directions:
      row, col = list(map(add, src, d))
      if not visited[src] and maze[row][col] == 0:
        ans = dfs([row, col], dest, maze, cost + 1, visited)
        if ans >= 0:
          return ans

    return -1
    
def process(start, end, maze):
