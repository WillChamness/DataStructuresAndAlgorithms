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

    
    def _percolate_up(self, index):
        def swap(li, i1, i2):
            temp = li[i1]
            li[i1] = li[i2]
            li[i2] = temp

        if not self._has_parent(index): # do nothing if you reached the top
            return
        if self.heap[index] > self.heap[self._parent_index(index)]: # do nothing if the parent is less than the child
            return
        
        swap(self.heap, index, self._parent_index(index))
        self._percolate_up(self._parent_index(index))
       

    def remove_min(self):
        if self.is_empty():
            raise Exception("MinHeap is empty.")

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
        def min(li, i1, i2):
            if li[i1] < li[i2]:
                return i1
            else:
                return i2

        if not self._has_left_child(index): # heap is inserted from left to right, so if there is no left child, the node must be a leaf
            return
        if not self._has_right_child(index): # node is parent of left leaf node only
            if index != min(self.heap, index, self._left_child_index(index)): # left child is smaller than parent
                swap(self.heap, index, self._left_child_index(index)) 
            return
        # otherwise the hole has two children

        # minimum of parent and two children
        min_index = min(self.heap, index, min(self.heap, self._left_child_index(index), 
            self._right_child_index(index)))
        if min_index == self._left_child_index(index): # case where left child is smallest
            swap(self.heap, index, self._left_child_index(index))
            self._percolate_down(self._left_child_index(index))
        elif min_index == self._right_child_index(index): # case where right child is smallest
            swap(self.heap, index, self._right_child_index(index))
            self._percolate_down(self._right_child_index(index))


    @staticmethod
    def heapify(li):
        def swap(li, i1, i2):
            temp = li[i1]
            li[i1] = li[i2]
            li[i2] = temp
        def percolate_up(li, index):
            parent_index = (index - 1) // 2

            if parent_index < 0: return # has no parent
            if li[index] > li[parent_index]: return # parent is smaller
            swap(li, index, parent_index)
            percolate_up(li, parent_index)
        
        for n in range(len(li)):
            percolate_up(li, n)
        
        return li


def main():
    import random as r
    h = MinHeap()
    l = []
    for i in range(10): 
        l.append(r.randint(0, 100))

    print(f"Before: {l}")
    for item in l: 
        h.insert(item)
    l = []

    while not h.is_empty(): 
        l.append(h.remove_min())
    print(f"After: {l}")

    l = []
    for i in range(11): 
        l.append(r.randint(0, 100))

    print(f"\nBefore: {l}")
    h = MinHeap(len(l), MinHeap.heapify(l))
    l = []
    while not h.is_empty(): 
        l.append(h.remove_min())
    print(f"After: {l}")

    print("\nThis will cause an exception: ")
    h.remove_min()


if __name__ == "__main__":
    main()