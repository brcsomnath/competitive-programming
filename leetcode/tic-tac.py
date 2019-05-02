'''
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

'''

class TicTacToe():
    def __init__(self, n):
        self.board = [[-1]* n]* n

    def move(x, y, choice):
        self.board[x][y] = choice

        for i in range(len(self.board[0])):
            if self.board[x][i] != choice 
                return 0
        

        for i in range(len(self.board[0])):
            if self.board[i][x] != choice 
                return 0
        
        return 1