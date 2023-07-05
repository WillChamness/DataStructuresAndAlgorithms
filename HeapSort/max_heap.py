class MaxHeap():
    @staticmethod
    def heapify(li):
        def swap(li, i1, i2):
            temp = li[i1]
            li[i1] = li[i2]
            li[i2] = temp
        def percolate_up(li, index):
            parent_index = (index - 1) // 2

            if parent_index < 0: return
            if li[index] < li[parent_index]: return

            swap(li, index, parent_index)
            percolate_up(li, parent_index)
        
        for n in range(len(li)):
            percolate_up(li, n)
        
        return li