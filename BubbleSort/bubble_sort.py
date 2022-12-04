def bubble_sort(li, recurisve=True):
    """ 
    Idea:
    Get the larger values closer to the right of the list by
    continuously swapping the current item with the next if the
    current item is greater.
    """
    if recurisve:
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