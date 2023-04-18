def bubble_sort(li, recursive=True):
    """ 
    Idea:
    Get the larger values closer to the right of the list by
    continuously swapping the current item with the next if the
    current item is greater.

    Strategy:
    Compare the item at index i to the item at index i+1. If the 
    item at index i is larger, swap. Then continue the process for
    item i+1. Repeat this strategy n times.

    Example:
    Given [3, 1, 4, 2, 0].

    Consider the sublist from index 0 to 4: [3, 1, 4, 2, 0]. Start 
    at index 0. Compare to the item at index 1. 3 > 1, so swap them.
    Now you have [1, 3, 4, 2, 0]. Compare the item at index 1 to 
    the item at index 2. 3 <= 4, so don't do anything. Now you have
    [1, 3, 4, 2, 0]. Compare the item at index 2 to the item at index 3.
    4 > 2, so swap them. Now you have [1, 3, 2, 4, 0]. Compare the item 
    at index 3 to index 4. 4 > 0, so swap the two. Now you have
    [1, 3, 2, 0, 4]. You have reached the end of the sublist. Therefore
    the item at index 4 is in the correct position. Reflect this in the 
    original list: [1, 3, 2, 0, 4].

    Consider the sublist from index 0 to 3: [1, 3, 2, 0]. Start at index
    0. Compare to the item at index 1. 1 <= 3, so don't do anything. Now
    you have [1, 3, 2, 0]. Compare the item at index 1 to the item at
    index 2. 3 > 2, so swap them. Now you have [1, 2, 3, 0]. Compare 
    the item at index 2 to the item at index 3. 3 > 0, so swap them.
    Now you have [1, 2, 0, 3]. You have reached the end of the sublist.
    Therefore the item at index 3 is in the correct position. Reflect this in 
    the original list: [1, 2, 0, 3, 4].

    Consider the sublist from index 0 to 2: [1, 2, 0]. Start at index 0. 
    Compare to the item at index 1. 1 <= 2, so don't do anything. Now 
    you have [1, 2, 0]. Compare the item at index 1 to the item at index 2.
    2 > 0, so swap them. Now you have [1, 0, 2]. You have reached the end 
    of the sublist. Therefore the item at index 2 is in the correct position.
    Reflect this in the original list: [1, 0, 2, 3, 4].

    Consider the sublist from index 0 to 1: [1, 0]. Start at index 0. 
    Compare to the item at index 1. i > 0, so swap the two. You have reached 
    the end of the sublist. Therefore the item at index 1 is in the correct
    position. Reflect this in the original list: [0, 1, 2, 3, 4]

    Consider the sublist from index 0 to 0: [0]. It is trivially the case
    that this sublist is sorted. No need to make any changes.

    We have considered all necessary sublists. Therefore the list is now sorted.
    """
    if recursive:
        _bubble_sort_rec(li, 0, len(li) - 1)
    else:
        _bubble_sort(li)


def _bubble_sort(li):
    for i in range(len(li) - 1, -1, -1): # consider the sublist from 0 to i (stop at i-1 because you will access i-1 + 1 later)
        for j in range(i): # go until you reach the end of the sublist
            if li[j] > li[j+1]: # if the current item is greater than the next, swap the two
                _swap(li, j, j+1)


def _bubble_sort_rec(li, current_index, last_index):
    if last_index <= 0: # if you have reached the trivial case, you are done
        return
    if current_index >= last_index: # if you have reached the end of the sublist, continue to the next sublist
        _bubble_sort_rec(li, 0, last_index - 1)
        return
    
    if li[current_index] > li[current_index + 1]: # swap if the current item is greater than the next
        _swap(li, current_index, current_index + 1)

    _bubble_sort_rec(li, current_index + 1, last_index) # regardless of if you swapped, move to the next item


def _swap(li, i1, i2):
    temp = li[i1]
    li[i1] = li[i2]
    li[i2] = temp


def main():
    import random as r
    l = []
    for i in range(10): l.append(r.randint(0, 100))
    print(f"Before: {l}")
    bubble_sort(l, False) # iterative bubble sort
    print(f"After: {l}")

    l = []
    for i in range(10): l.append(r.randint(0, 100))
    print(f"\nBefore: {l}")
    bubble_sort(l) # recursive bubble sort
    print(f"After: {l}")

if __name__ == "__main__":
    main()