'''
Build a text editor class with the following functions,

moveCursorLeft(),

moveCursorRight(),

insertCharacter(char) //insert the char right before cursor

backspace() //delete the char right before cursor

Follow-up
Implement undo() //undo the last edit. Can be called multiple times until all edits are cancelled.

All functions above should take O(1) time.
'''


class TextEditor(object):
    def __init__(self):
        self.word = ""
        self.cursor = 0
        self.undo = []
    
    def moveCursorLeft(self):
        if self.cursor != 0:
            self.cursor -= 1
        self.undo.append(('RIGHT', ''))
    
    def moveCursorRight(self):
        if self.cursor != len(self.word):
            self.word += 1
        self.undo.append(('LEFT', ''))
    
    def insertCharacter(self, char):
        self.word = self.word[:self.cursor] + str(char) + self.word[self.cursor:]
        self.cursor += 1
        self.undo.append(('DEL', char))
    
    def backspace(self):
        if len(self.word) == 0:
            self.undo.append(('INS', self.word[self.cursor - 1]))
        self.word = self.word[:self.cursor-1] + self.word[self.cursor:]
        if self.cursor != 0:
            self.cursor -= 1
        
    def undo_op(self):
        op, char = self.undo.pop()
        
        if op == 'RIGHT':
            self.moveCursorRight()
        elif op == 'LEFT':
            self.moveCursorLeft()
        elif op == 'DEL':
            self.backspace()
        elif op == 'INS':
            self.insertCharacter(char)

    
    def getWord(self):
        return self.word[:self.cursor] + '|' + self.word[self.cursor:]