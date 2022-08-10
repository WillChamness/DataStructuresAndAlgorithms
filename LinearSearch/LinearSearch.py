def linear_search(li, target, choice="recursive"):
    if choice == "recursive":
        return __linear_search_rec__(li, target, 0)
    else:
        return __linear_search__(li, target)


def __linear_search__(li, target):
    for i in range(len(li) - 1):
        if li[i] == target:
            return i
    return -1


def __linear_search_rec__(li, target, index):
    if index < 0 or len(li) <= index:
        return -1
    if li[index] == target:
        return index
    else:
        return __linear_search_rec__(li, target, index + 1)


def main():
    l1 = [1,2,3,4,5,6,7,8,9]
    l2 = [1,2,3,4,5,6,7,8,9,10]
    print(linear_search(l1, 7))
    print(linear_search(l2, 5))
    print(linear_search([], 1000))
    print(linear_search(l2, 1000))
    print(linear_search(l1, 7, "a"))
    print(linear_search(l2, 5, "a"))
    print(linear_search(l2, 1000, "a"))
    print(linear_search([], 10000, "a"))




if __name__ == "__main__":
    main()