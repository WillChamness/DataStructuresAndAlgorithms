def merge_sort(li):
    if len(li) <= 1: 
        return
    
    left_sublist = [None] * (len(li) // 2) 
    right_sublist = [None] * (len(li) - len(left_sublist)) 

    for i in range(0, len(left_sublist)):
        left_sublist[i] = li[i]

    for i in range(len(left_sublist), len(li)):
        right_sublist[i - len(left_sublist)] = li[i] 

    merge_sort(left_sublist)
    merge_sort(right_sublist)
    _merge(li, left_sublist, right_sublist)