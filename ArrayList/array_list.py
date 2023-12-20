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


    def resize(self, factor):
        self.size *= factor
        new_array = [None] * self.size

        for i in range(self.pointer):
            new_array[i] = self.array[i]
        
        self.array = new_array


    def get(self, index):
        return self.array[index]
    

    def find(self, target):
        return linear_search(self.array, target, self.pointer)


    def __str__(self):
        s = "["
        for i, item in enumerate(self.array):
            if i <= self.pointer - 1:
                s += str(item) + ", "
            else:
                s += "_, "
        return s[:len(s) - 2] + "]"
    

    def __repr__(self):
        s = "["
        for i, item in enumerate(self.array):
            if i == self.pointer - 1:
                s += "***" + str(item) + "***, "
            else:
                s += str(item) + ", "
                
        return s[:len(s) - 2] + "]"


def main():
    import random as rd
    lst = ArrayList()

    print("Adding 11 items:")
    for _ in range(10):
        lst.add(rd.randint(0, 99))
    print(lst)
    lst.add(-1)
    print(lst)

    print("\nRemoving items:")
    print("5th item in list:", lst.remove(5))
    print("last item in list:", lst.remove_last())
    print(repr(lst))
    print(lst)

    print("\nOverwriting data marked deleted:")
    lst.add(1000)
    lst.add(1001)
    lst.add(1002)
    print(repr(lst))

    print("\nSearching for items:")
    print("Index of value 1000:", lst.find(1000))
    print("Index of value 5000:", lst.find(5000))
    lst.remove_last()
    print("Index of a value marked deleted:", lst.find(1002))


if __name__ == "__main__":
    main()