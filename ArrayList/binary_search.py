def binary_search(sorted_list, target, end, recursive=False):
    if recursive:
        return _binary_search_rec(sorted_list, target, 0, end - 1)
    else:
        return _binary_search(sorted_list, target, end)


def _binary_search(l, target, end):
    lo = 0
    hi = end - 1

    while not (lo > hi):  
        mid = (lo + hi) // 2
        if l[mid] == target:  
            return mid
        elif target < l[mid]:  
            hi = mid - 1
        else:  
            lo = mid + 1

    return -1  


def _binary_search_rec(l, target, lo, hi):
    if lo > hi:  
        return -1

    mid = (lo + hi) // 2
    if l[mid] == target: 
        return mid 
    elif target < l[mid]:
        return _binary_search_rec(l, target, lo, mid - 1) 
    else: 
        return _binary_search_rec(l, target, mid + 1, hi)

