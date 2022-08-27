def linear_search(li, target, choice="recursive"):
    """ 
    Searches a list of size n.
    Time complexity: O(n)
    Space complexity: O(1)

    Idea:
    Search the list one-by-one until you find the target. Unlike binary
    search, linear search does not require the list to be sorted.

    Strategy:
    Starting at index 0, compare the item to the target. If they are equal,
    the target has been found. Otherwise, check the next item in the list.
    Continue until either the target has been found or you have reached
    the end of the list.


    Example:
    Given [2, 4, 0, 3, 1]. Search for the number 3.

    Start at the beginning. 3 != 2, so check the next item. 3 != 4, so
    check the next item. 3 != 0, so check the next item. 3 == 3, so
    the target has been found.
    """

    if choice == "recursive":
        return __linear_search_rec__(li, target, 0)
    else:
        return __linear_search__(li, target)


def __linear_search__(li, target):
    # iterate through the list until the target has been found
    for i in range(len(li)): 
        if li[i] == target:
            return i
    return -1 # target not found


def __linear_search_rec__(li, target, index):
    if index < 0 or len(li) <= index: # continue until you are out of bounds
        return -1
    if li[index] == target: # target found, return its index
        return index
    else: # target not found, search the next item in the list
        return __linear_search_rec__(li, target, index + 1)


def main():
    l1 = [1,2,3,4,5,6,7,8,9]
    l2 = [1,2,3,4,5,6,7,8,9,10]
    print(linear_search(l2, 5)) # index 4
    print(linear_search([], 1000)) # not found; -1
    print(linear_search(l2, 1000)) # not found; -1
    print(linear_search(l1, 7, "a")) # index 6
    print(linear_search(l2, 5, "a")) # index 4
    print(linear_search(l2, 1000, "a")) # not found; -1
    print(linear_search([], 10000, "a")) # not found; -1




if __name__ == "__main__":
    main()