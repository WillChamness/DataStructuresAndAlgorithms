class ArrayList:
    def __init__(self, initial_size=10, initial_item=None):
        self.size = initial_size
        self.array = [None] * initial_size
        self.pointer = 0

        if initial_item is not None:
            self.add(initial_item)


    def add(self, item):
        if self.pointer >= self.size:
            self.resize(2)
        
        self.array[self.pointer] = item
        self.pointer += 1
 

    def remove(self, index):
        if index >= self.pointer:
            return None
        if index < 0:
            return None
        
        current = index
        item = self.array[index]


    def remove_last(self):
        if self.pointer <= 0:
            return None
        
        self.pointer -= 1
        return self.array[self.pointer]


    def _swap(self, li, i, j):
        tmp = li[i]
        li[i] = li[j]
        li[j] = tmp