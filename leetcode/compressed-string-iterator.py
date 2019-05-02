'''
604. Design Compressed String Iterator

Design and implement a data structure for a compressed string iterator. 
It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive
 integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; 
Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, 
as static/class variables are persisted across multiple test cases. Please see here for more details.
'''

class StringIterator():
    def __init__(self, string):
        self.word = string
        self.index = 0
        self.letter = self.word[0]
        self.count = self.get_count(self.index + 1)

    def get_count(self, idx):
        num = 0
        while idx < len(self.word) and self.word[idx].isdigit():
            num = num*10 + int(ord(self.word[idx]) - ord('0'))
            idx += 1
        self.index = idx
        return num

    def hasNext(self):
        if self.count == 0 and self.index == len(self.word):
            return False
        return True
    
    def next(self):
        # print(self.count)
        if self.count > 0:
            self.count -= 1
            return self.letter
        
        if self.index >= len(self.word):
            return ''
        
        self.letter = self.word[self.index]
        self.count = self.get_count(self.index + 1)
        return self.next()


if __name__ == "__main__":
    
    iterator = StringIterator("L1e2t1C1o1d1e1") 

    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())