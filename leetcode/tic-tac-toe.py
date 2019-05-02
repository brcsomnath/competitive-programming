'''
348. Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |
'''

class TicTacToe():
    def __init__(self, N):
        self.N = N
        self.rows = [0 for in range(N)]
        self.cols = [0 for in range(N)]
        self.diag = 0
        self.xdiag = 0
    
    def move(self, row, col, player):
        p = 1 if player & 1 else -1
        
        self.rows[row] += p
        self.cols[col] += p

        if row == col:
            self.diag += p

        if row + col == len(self.rows) - 1:
            self.xdiag += p
        
        if abs(self.rows[row]) == self.N or abs(self.cols[col]) == self.N or abs(self.diag) == self.N or abs(self.xdiag) == N:
            return p if p == 1 else 2
        
        return -1
