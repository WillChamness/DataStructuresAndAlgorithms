class Heap:
    def __init__(self, capacity=10, heap=None):
        self.heap = heap
        self.capacity = capacity
        self.size = 0
        if heap is None:
            self.heap = [None] * capacity
        else:
            for i in range(len(self.heap)):
                if heap[i] is not None and self.size < self.capacity:
                    self.size += 1
                else:
                    break


    def _parent_index(self, child_index):
        return (child_index - 1) // 2 
    

    def _left_child_index(self, parent_index):
        return 2*parent_index + 1
    

    def _right_child_index(self, parent_index):
        return 2*parent_index + 2


    def _has_parent(self, child_index):
        return self._parent_index(child_index) >= 0


    def _has_left_child(self, parent_index):
        return self._left_child_index(parent_index) < self.size


    def _has_right_child(self, parent_index):
        return self._right_child_index(parent_index) < self.size


    def _next_empty_slot(self):
        return self.size


    def is_full(self):
        return self.size == self.capacity


    def is_empty(self):
        return self.size == 0


    def insert(self):
        pass


    def remove_min(self):
        pass


    def remove_max(self):
        pass


    def _percolate_up(self):
        pass


    def _percolate_down(self):
        pass