from array_list import ArrayList
from binary_search import binary_search

class SortedArrayList(ArrayList):
    def __init__(self, initial_size=10, initial_item=None):
        super().__init__(initial_size, initial_item)
    

    def add(self, item):
        """
        Adds the item to the end, then performs the best-case
        insertion sort algorithm (array is almost sorted).

        Worst-case time complexity: O(n)
        Average time complexity: O(n)
        Worst-case space complexity: O(n)
        Average space complexity: O(1)
        """
        super().add(item)
        
        # perform best-case insertion sort after adding - O(n) time complexity
        index = self.pointer - 1
        while index > 0 and item < self.array[index - 1]:
            super()._swap(self.array, index, index - 1)
            index -= 1


    def remove(self, index):
        """
        Removes the value at the index, then ensures that
        the array is sorted by iteratively swapping 
        until the end of the list is reached.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        if index < 0 or index >= self.pointer:
            return None
        
        # push the item "out of bounds" to maintain sorted order
        current = index

        while current < self.pointer - 1:
            super()._swap(self.array, current, current+1)
            current += 1
        
        return super().remove_last()
    

    def find(self, target):
        """
        Can use binary search since the array is sorted.

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        return binary_search(self.array, target, end=self.pointer)



def main():
    import random as rd
    lst = SortedArrayList()

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