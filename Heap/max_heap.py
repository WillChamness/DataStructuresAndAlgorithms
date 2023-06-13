from heap import Heap


class MaxHeap(Heap):
    def __init__(self, capacity=10, initial_heap=None):
        Heap.__init__(self, capacity, initial_heap)

    
    def insert(self, item):
        if self.is_full():
            raise Exception("MaxHeap is full.")

        self.heap[self._next_empty_slot()] = item
        self._percolate_up(self._next_empty_slot())
        self.size += 1


    def _percolate_up(self, index):
        def swap(li, i1, i2):
            temp = li[i1]
            li[i1] = li[i2]
            li[i2] = temp

        if not self._has_parent(index): # do nothing if you reached the top
            return
        if self.heap[index] < self.heap[self._parent_index(index)]: # do nothing if parent is greater than child
            return
        
        swap(self.heap, index, self._parent_index(index))
        self._percolate_up(self._parent_index(index))