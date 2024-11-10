from insertion_sort import insertion_sort
from insertion_sort import partial_insertion_sort

def quick_sort(li, cutoff=10):
    """
    Driver for recursive quick sort.
    """
    _quick_sort(li, 0, len(li) - 1, cutoff)

def _quick_sort(li, low_index, high_index, cutoff):
    """ 
    Extremely fast sorting algorithm in the average case. Although the 
    worst case time complexity is worse than merge sort and heap sort, 
    quick sort is extremely optimized in the average case and thus
    is more popular.

    Average time complexity: O(n*log(n))
    Worst-case time complexity: O(n^2)
    Space complexity: O(1)

    Idea:
    Choose some number to be the "pivot." Then partition the list. Recursively
    perform quick sort until you reach a cutoff. Then sort the rest of the list
    with insertion sort. 
    """
    if high_index - low_index <= cutoff:
        partial_insertion_sort(li, low_index, high_index)
        return

    _swap(li, _median_of_3(li, low_index, high_index), high_index) # swap last item with median of first, last and middle item
    last_pivot_index = _partition(li, low_index, high_index) 
    _quick_sort(li, low_index, last_pivot_index - 1, cutoff)
    _quick_sort(li, last_pivot_index + 1, high_index, cutoff)

def _partition(li, low_index, high_index):
    """ 
    Partitions a list into two sublists. All items in the list less than the "pivot" 
    are pushed to the left, and all items greater than the pivot are pushed to the
    right. The pivot is chosen to be whatever the last index is in the sublist. As
    shown by _quick_sort(), the last index is the median of three numbers.

    Idea:
    Try to (somehow) create a partition of the pivot, items less than the pivot,
    and the items greater than the pivot.

    Strategy:
    Start at the beginning of the list. Iteratively walk from left to right until you
    find a number greater than the pivot. Then swap the two. Repeat this process until 
    the left and right indeces meet.

    Example:
    Given [3, 0, 1, 4, 2].

    Choose p = 2 (the last item in the sublist). Find the minimum index of any number 
    greater than p: 0. Then find the *minimum index* of any number *greater than* p: 0. 
    Then find the **maximum index** of any number **less than** p: 2. 0 < 2, so swap the items
    at index 0 and index 2. The list now looks like this: [1, 0, 3, 4, 2]. 

    Find the minimum index > 0 of any number greater than p: 2. Then find the maximum index < 2
    of any number less than p: 1. 2 >= 1, so the list is partitioned: [[1, 0], [3, 4], [2]].
    
    Lastly, reorganize the partition so that the pivot is in between the other sublists:
    [[1, 0], [2], [3, 4]]
    """
    left = low_index
    right = high_index
    pivot = li[high_index]

    while left < right:
        # find number that is greater than pivot
        while li[left] <= pivot: 
            if left < right: # must check because it is possible to walk past right
                left += 1
            else:
                break

        # find the number that is less than the pivot
        while li[right] >= pivot:
            if left < right: # likewise, it is possible to walk past left
                right -= 1 
            else:
                break
        
        _swap(li, left, right)

    _swap(li, left, high_index)
    return left


def _median_of_3(li, lo, hi):
    """
    Method of choosing the pivot is to take the median of 3 numbers
    in the list and swapping it with the last index. Although this
    method doesn't guarantee that a good pivot will always be
    chosen, it does make a significant difference in the average
    case
    """
    temp = [li[lo], li[hi], li[(lo + hi) // 2]]
    insertion_sort(temp)
    if temp[1] == li[lo]:
        return lo
    elif temp[1] == li[hi]:
        return hi
    else:
        return (lo + hi) // 2

def _swap(li, index1, index2):
    temp = li[index1]
    li[index1] = li[index2]
    li[index2] = temp

def _alt_partition(li, lo, hi):
    """ 
    Alternative partitioning method that is more readable,
    but increases space complexity to O(n)
    """
    less = [None] * len(li)
    greater = [None] * len(li)
    pivot = [li[len(li) - 1]]
    less_i = 0
    greater_i = 0

    for i in range(len(li)):
        # Move all numbers less than the pivot to a temp array
        if li[i] < pivot[0]:
            less[less_i] = li[i]
            less_i += 1
        # Move all numbers greater than the pivot to a temp array
        else:
            greater[greater_i] = li[i]
            greater += 1
    
    # Copy all numbers less than the pivot to the left of the array
    current = 0
    for i in range(less_i + 1):
        li[current] = less[i]
        current += 1
    
    # Copy all numbers greater than the pivot to the right of the array
    for i in range(greater_i + 1):
        li[current] = greater[i]
        current += 1

    li[current] = pivot[0]



def main():
    import random as rd 
    l = list(rd.randint(0,100) for i in range(50))
    print("Before:", l)
    quick_sort(l)
    print("After:", l)

    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            print("List not sorted")
            break
    else:
        print("List sorted correctly")

if __name__ == "__main__":
    main()