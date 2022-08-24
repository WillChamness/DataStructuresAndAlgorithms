def insertion_sort(li):
    """
    Sorts a list of length n.
    Time complexity: O(n^2)
    Space complexity: O(1)

    Idea: 
    Starting at the beginning, move the current item after an item lesser than itself
    (or to the first position). Then do the same with the item after. This process
    is similar to how you would sort a deck of cards.

    Strategy:
    For every item in the list, compare to the item before it (if possible).
    If the item is less than the previous one, swap the two. Continue this process
    until the item is either the first in the list or greater than or equal to the previous.


    Example:
    Given [3, 1, 2, 4, 0].

    Consider the sublist from index 0 to 0: [3]. It is trivially
    the case that this list is sorted. No need to make any changes.

    Consider the sublist from index 0 to 1: [3, 1]. Start at the end. 
    Compare to the previous value. 1 < 3, so swap the two. Now you have
    [1, 3]. Now 1 is at the beginning of the list, so the list is sorted.
    Refect this in the original list: [1, 3, 2, 4, 0].

    Consider the sublist from index 0 to 2: [1, 3, 2]. Start at the end.
    Compare to the previous value. 2 < 3, so swap the two. Now you have
    [1, 2, 3]. Check the previous value. 2 >= 1, so the entire list is
    sorted. Reflect this is the original list: [1, 2, 3, 4, 0].

    Consider the sublist from index 0 to 3: [1, 2, 3, 4]. Start at the end.
    Compare to the previous value. 4 >= 3, so the entire list is sorted. Reflect
    this in the original list: [1, 2, 3, 4, 0].

    Consider the sublist from index 0 to 4: [1, 2, 3, 4, 0]. Start at the end.
    Compare to the previous value. 0 < 4, so swap the two. Now you have
    [1, 2, 3, 0, 4]. Check the previous value. 0 < 3, so swap the two. Now
    you have [1, 2, 0, 3, 4]. Check the previous value. 0 < 2, so swap the two.
    Now you have [1, 0, 2, 3, 4]. Check the previous value. 0 < 1, so swap the two.
    Now you have [0, 1, 2, 3, 4]. 0 is at the front of the list, so the entire list
    is sorted. Reflect this in the original list: [0, 1, 2, 3, 4]

    We have considered all necessary sublists. Therefore the list is sorted.
    """

    # Method for swapping
    def swap(li, index1, index2):
        temp = li[index1]
        li[index1] = li[index2]
        li[index2] = temp
    
    for i in range(1, len(li)): # Consider the sublist from 0 to i (no need to consider the sublist from 0 to 0). 
        for j in range(i, 0, -1): # start at the end of the sublist, move pointer left if swapped and stop if the pointer reaches 0.
            # move this object left if it is less than the previous. Then repeat.
            if li[j] < li[j-1]: 
                swap(li, j, j-1)
            # otherwise, you have sorted everything to the left of i. No need to continue this iteration. 
            else:
                break


def main():
    import random as r 
    l = []
    for k in range(10):
        l.append(r.randint(0, 100))
    print("Before: " + str(l))
    insertion_sort(l)
    print("After: " + str(l))

if __name__ == "__main__":
    main()