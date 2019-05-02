'''
353. Design Snake Game


Design a Snake game that is played on a device with screen size = width x height.
Play the game online if you are not familiar with the game.
The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
You are given a list of food's positions in row-column order. When a snake eats the food,
its length and the game's score both increase by 1. Each food appears one by one 
on the screen. For example, the second food will not appear until the first food
was eaten by the snake.When a food does appear on the screen, it is guaranteed that
it will not appear on a block occupied by the snake.
'''

class Snake():
    def __init__(self, width, height, food):
        self.w = width
        self.h = height
        self.food = food
        self.head = [0, 0]
        self.length = 1

    def move(self, step):
        if step == 'L':
            self.head[0] -= 1
        elif step == 'R':
            self.head[0] += 1
        elif step == 'U':
            self.head[1] -= 1
        elif step == 'D':
            self.head[1] += 1
        
        if self.head[0] < 0 or self.head[0] >= self.w or self.head[1] < 0 or self.head[1] >= self.h:
            return -1

        if self.head == self.food[-1]:
            self.food.pop()
            self.length += 1
            
        return self.length - 1