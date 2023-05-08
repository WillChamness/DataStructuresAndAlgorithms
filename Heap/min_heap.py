from heap import Heap

class MinHeap(Heap):
    def __init__(self, capacity=10, initial_heap=None):
        Heap.__init__(self, capacity, initial_heap)

    def insert(self, item):
        if self.is_full():
            raise Exception("MinHeap is full.")
        
        self.heap[self._next_empty_slot()] = item
        self._percolate_up(self._next_empty_slot())
        self.size += 1