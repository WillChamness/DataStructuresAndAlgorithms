def linear_search(arr, target, end, recursive=False):
    if recursive:
        return _linear_search_rec(arr, target, end, 0)
    else:
        return _linear_search(arr, target, end)


def _linear_search(arr, target, end):
    for i in range(end): 
        if arr[i] == target:
            return i
    return -1 


def _linear_search_rec(arr, target, end, index):
    if index < 0 or end <= index: 
        return -1
    if arr[index] == target: 
        return index
    else: 
        return _linear_search_rec(arr, target, end, index + 1)

