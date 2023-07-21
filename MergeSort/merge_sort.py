def merge_sort(li):
    """ 
    Time complexity: O(n*log(n))
    Space complexity: O(n)

    You can do an in-place sort to reduce the space complexity to O(1), but the 
    time complexity gets increased to O(n^2*log(n)). At that point, you should
    use insertion sort instead.
    """
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


def _merge(li, left_sublist, right_sublist):
    left_pointer = 0
    right_pointer = 0
    list_pointer = 0

    while left_pointer < len(left_sublist) and right_pointer < len(right_sublist):
        left_num = left_sublist[left_pointer]
        right_num = right_sublist[right_pointer]

        if left_num < right_num:
            li[list_pointer] = left_num
            left_pointer += 1
        else:
            li[list_pointer] = right_num
            right_pointer += 1
        list_pointer += 1
    
    while left_pointer < len(left_sublist):
        li[list_pointer] = left_sublist[left_pointer]
        left_pointer += 1
        list_pointer += 1

    while right_pointer < len(right_sublist):
        li[list_pointer] = right_sublist[right_pointer]
        right_pointer += 1
        list_pointer += 1



def main():
    import random as r 
    l = []

    for i in range(10):
        l.append(r.randint(0, 100))

    print(f"Before: {l}")
    merge_sort(l)
    print(f"After: {l}")

    l = []
    for i in range(11):
        l.append(r.randint(0, 100))
    print(f"\nBefore: {l}")
    merge_sort(l)
    print(f"After: {l}")


if __name__ == "__main__":
    main()