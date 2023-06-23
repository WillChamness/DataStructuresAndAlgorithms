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


    def remove_max(self):
        if self.is_empty():
            raise Exception("MaxHeap is empty.")
        
        item = self.heap[0]
        self.heap[0] = self.heap[self._next_empty_slot() - 1]
        self.size -= 1
        self._percolate_down(0)
        return item


    def _percolate_down(self, index):
        def swap(li, i1, i2):
            temp = li[i1]
            li[i1] = li[i2]
            li[i2] = temp
        def max(li, i1, i2):
            if li[i1] > li[i2]:
                return i1
            else:
                return i2

        if not self._has_left_child(index):
            return
        if not self._has_right_child(index):
            if index != max(self.heap, index, self._left_child_index(index)):
                swap(self.heap, index, self._left_child_index(index))
            return
        
        max_index = max(self.heap, index, max(self.heap, self._left_child_index(index), 
            self._right_child_index(index)))
        if max_index == self._left_child_index(index):
            swap(self.heap, index, self._left_child_index(index))
            self._percolate_down(self._left_child_index(index))
        elif max_index == self._right_child_index(index):
            swap(self.heap, index, self._right_child_index(index))
            self._percolate_down(self._right_child_index(index))