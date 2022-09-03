def binary_search(sorted_list, target, choice="recursive"):
    """
    Searches a sorted list of size n.
    Time complexity: O(log(n))
    Space complexity: O(1)

    Idea:
    Divide and conquer. Subdivide the sorted list until the target is found
    or until there is nothing else to search.

    Strategy:
    Compare the target with the item in the middle of the array. If the target
    is equal to the item, the target has been found. If the target is less than 
    the item, the target is in the left half. Otherwise, the target is in the
    right half. Continue to divide and conquer until either the target has
    been found or there is nothing left to search.


    Example:
    Given [0, 1, 2, 3, 4]. Search the list for the number 3.
    
    Begin at the middle index (index 2). 3 > 2, so if 3 is in the list, it will be to 
    the right of 2. Now consider the sublist containing all items to the right
    of 2: [3. 4]. 
    
    Begin at the middle index (index 0.5). We will arbitrarily round down since the middle
    index is not an integer. 3 == 3, so we have found the target. 
    """

    if choice == "recursive":
        return __binary_search_rec__(sorted_list, target, 0, len(sorted_list) - 1)
    else:
        return __binary_search__(sorted_list, target)


def __binary_search__(l, target):
    lo = 0
    hi = len(l) - 1

    while not (lo > hi): # continue until there is nothing left to search
        mid = (lo + hi) // 2
        if l[mid] == target: # target found, return its index
            return mid
        elif target < l[mid]: # target is in the left half of the sublist, update pointers
            hi = mid - 1
        else: # target is in the right half of the sublist, update pointers
            lo = mid + 1 
    
    return -1 # target not found


def __binary_search_rec__(l, target, lo, hi):
    if lo > hi: # continue until there is nothing left to search
        return -1
    
    mid = (lo + hi) // 2
    if l[mid] == target: # target found, return its index
        return mid
    elif target < l[mid]: # target is in the left half, perform binary search on the left half of the sublist
        return __binary_search_rec__(l, target, lo, mid - 1)
    else:
        return __binary_search_rec__(l, target, mid + 1, hi) # target is in the right half, perform binary search on the right half of the sublist
    

        

def main():
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(list1, 2)) # index 1
    print(binary_search(list1, 10)) # not found; -1
    print(binary_search(list2, 10)) # 9
    print(binary_search(list2, 1)) # 0
    print(binary_search([], 1000)) # not found; -1
    print(binary_search(list1, 3, "a")) # 2
    print(binary_search(list1, 9, "a")) # 8
    print(binary_search(list2, 3, "a")) # 2
    print(binary_search(list2, 9, "a")) # 8
    print(binary_search([], 10, "a")) # not found; -1


if __name__ == "__main__":
    main()