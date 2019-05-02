import sys

class Heap():
    def __init__(self, size):
        self.heap = [-1]*size
        self.HEAP_SIZE = 0


    def heapify(self, index):
        """
        Top down approach
        To check Min heap property
        """

        left = 2*index + 1
        right = 2*index + 2

        min_ind = index
        if left < self.HEAP_SIZE and self.heap[left] < self.heap[min_ind]:
            min_ind = left
        
        if right < self.HEAP_SIZE and self.heap[right] < self.heap[min_ind]:
            min_ind = right

        if min_ind != index:
            self.heap[index], self.heap[min_ind] = self.heap[min_ind], self.heap[index]
            self.heapify(min_ind)

    def get_min(self):
        """
        Extract minimum element from Heap
        Maintain Heap property
        """

        small = self.heap[0]
        self.heap[0] = self.heap[self.HEAP_SIZE - 1]
        self.HEAP_SIZE -= 1

        self.heapify(0)
        return small

    def parent(self, index):
        """
        Returns index of parent node
        """

        return int(index/2)

    def bottom_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def insert(self, value):
        """
        Insert value into Heap
        Adjust heap property using bottom up approach
        """

        self.HEAP_SIZE += 1
        self.heap[self.HEAP_SIZE - 1] = value
        self.bottom_up(self.HEAP_SIZE - 1)

    def update(self, index, value):
        """
        Update value of index
        """

        if index >= self.HEAP_SIZE:
            return "FAILURE"
        
        self.heap[index] = value
        self.bottom_up(index)
        return "SUCCESS"

    def delete_key(self, index):
        self.update(index, -sys.maxsize-1)
        self.get_min()
    

def heap_util():
    h = Heap(100)
    h.insert(3)
    h.insert(2) 
    h.delete_key(1)
    h.insert(15)
    h.insert(5) 
    h.insert(4)
    h.insert(45)
    print(h.get_min())
    print(h.heap[0])
    h.update(2, 1)
    print(h.get_min())

if __name__ == "__main__":
    heap_util()