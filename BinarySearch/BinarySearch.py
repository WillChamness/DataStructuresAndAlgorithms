def binary_search(sorted_list, target, choice="recursive"):
    if choice == "recursive":
        return __binary_search_rec__(sorted_list, target, 0, len(sorted_list) - 1)
    else:
        return __binary_search__(sorted_list, target)

def __binary_search__(l, target):
    lo = 0
    hi = len(l) - 1

    while not (lo > hi):
        mid = (lo + hi) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return -1

def __binary_search_rec__(l, target, lo, hi):
    if lo > hi:
        return -1
    
    mid = (lo + hi) // 2
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return __binary_search_rec__(l, target, lo, mid - 1)
    else:
        return __binary_search_rec__(l, target, mid + 1, hi)
    
    return -1


        

def main():
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(list1, 3, "a"))
    print(binary_search(list1, 9, "a"))
    print(binary_search(list2, 3, "a"))
    print(binary_search(list2, 9, "a"))
    print(binary_search([], 10, "a"))


if __name__ == "__main__":
    main()