def selection_sort(li):
    """ 
    Sorts a list of size n.
    Time complexity: O(n^2)
    Space complexity: O(1)

    Strategy:
    For every item at index i, check all items to the right for the smallest item. Then swap
    the two. Repeat this process for index i + 1 until you have reached the end of the list.

    Example: 
    Given [3, 2, 1, 4, 0].

    Start at the beginning. Consider the sublist from index 0 to 4: [3, 1, 2, 4, 0]. Find the index
    of the minimum item in this sublist: 4. Then swap items at index 0 with index 4. Now you have 
    [0. 2. 1. 4. 3]. Reflect this in the original list: [0, 2, 1, 4, 3].

    Consider the sublist from index 1 to 4: [2, 1, 4, 3]. Find the index of the minimum item in this 
    sublist: 1. Then swap the items at index 0 with 1. Now you have [1, 2, 4, 3]. Reflect this
    in the original list: [0, 1, 2, 4, 3]. 

    Consider the sublist from index 2 to 4: [2, 4, 3]. Find the index of the minimum item in this sublist:
    0. Then swap the items at index 0 with 0. Now you have [2, 4, 3]. Reflect this in the original list:
    [0, 1, 2, 4, 3]

    Consider the sublist from index 3 to 4: [4, 3]. Find the index of the minimum item in this sublist:
    1. Then swap the items at index 0 with 1. Now you have [3, 4]. Reflect this in the original list:
    [0, 1, 2, 3, 4].

    Consider the sublist from index 4 to 4: [4]. It is trivially the case that this sublist is 
    sorted. No need to make any changes.

    We have considered all necessary sublists. Therefore the list is now sorted.
    """

    # Method for swapping
    def swap(li, index1, index2):
        temp = li[index1]
        li[index1] = li[index2]
        li[index2] = temp

    for i in range(len(li)): # consider the sublist from index i to len(li) - 1
        min_index = i # initially assume the minimum is at index i
        for j in range(i, len(li)): # check all items to the right of i for the smallest item
            if li[j] < li[min_index]: # update the minimum index as necessary
                min_index = j
        swap(li, i, min_index)


def main():
    import random as r
    l = []
    for k in range(10):
        l.append(r.randint(0, 100))
    print("Before:" + str(l))
    selection_sort(l)
    print("After: " + str(l))

if __name__ == "__main__":
    main()