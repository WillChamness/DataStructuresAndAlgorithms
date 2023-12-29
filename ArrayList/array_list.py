from linear_search import linear_search

class ArrayList:
    def __init__(self, initial_size=10, initial_item=None):
        self.size = initial_size
        self.array = [None] * initial_size
        self.pointer = 0

        if initial_item is not None:
            self.add(initial_item)


    def add(self, item):
        """
        Simply add the item to the end of the list.

        If the array is full, then create a new array and copy the
        old array to the new array.

        Worst-case time complexity: O(n)
        Average time complexity: O(1)
        Worst-case space complexity: O(n)
        Average space complexity: O(1)
        """
        if self.pointer >= self.size:
            self.resize(2)
        
        self.array[self.pointer] = item
        self.pointer += 1
 

    def remove(self, index):
        if index >= self.pointer:
            return None
        if index < 0:
            return None

        # put the item "out of bounds" by swapping with the last item.
        # if you want to maintain the original order of the list, 
        # you can push the item to the end by iteratively swapping
        # adjacent items, but this increases time complexity
        self._swap(self.array, index, self.pointer - 1)
        return self.remove_last()


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
    print(lst)
    print(repr(lst))

    print("\nOverwriting data marked deleted:")
    lst.add(1000)
    lst.add(1001)
    lst.add(1002)
    print(repr(lst))

    print("\nSearching for items:")
    print("Index of value 1000:", lst.find(1000))
    print("Index of value 5000:", lst.find(5000))
    lst.remove(lst.find(1002))
    print("Index of a value marked deleted:", lst.find(1002))


if __name__ == "__main__":
    main()