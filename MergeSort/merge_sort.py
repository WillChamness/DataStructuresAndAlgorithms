def merge_sort(li):
    """ 
    Time complexity: O(n*log(n))
    Space complexity: O(n)

    You can do an in-place sort to reduce the space complexity to O(1), but the 
    time complexity gets increased to O(n^2*log(n)). At that point, you should
    use insertion sort instead.

    Idea:
    Split the array into halves until you can't divide them anymore. Then 
    somehow merge the left and right subarrays such that the result is a 
    sorted array

    Example:
    Given [3, 2, 1, 4, 0]

    Split the array into two:
    [3, 2], [1, 4, 0]

    Split the left subarray into two:
    [[3], [2]]        [1, 4, 0]

    The two subarrays are trivially sorted. Therefore, merge the two:
    [2, 3]              [1, 4, 0]

    Split the right subarray into two:
    [2, 3]              [[1, 4], [0]]

    Split the right left subarray into two:
    [2, 3]              [ [[1], [4]], [0] ]

    The subarrays are trivially sorted. Therefore, merge the two:
    [2, 3]              [[1, 4], [0]]

    The subarrays are sorted. Therefore, merge the two:
    [2, 3]              [0, 1, 4]

    The subarrays are sorted. Therefore, merge the two:
    [0, 1, 2, 3, 4]
    """
    if len(li) <= 1: # list has at most 1 element and is trivially sorted
        return
    
    left_sublist = [None] * (len(li) // 2) # e.g. if n == 5, then left_sublist represents the first two items
    right_sublist = [None] * (len(li) - len(left_sublist)) # represents whatever isn't in left_sublist

    # copy left half into left sublist
    for i in range(0, len(left_sublist)):
        # e.g. len(li) == 5 ==> len(left_sublist) == 5 div 2 == 2, so
        # i == 0 ==> left_sublist[0] = li[0]
        # i == 1 ==> left_sublist[1] = li[1]
        # i == 2 ==> you are in the right sublist so stop
        left_sublist[i] = li[i]

    # copy right half into right sublist
    for i in range(len(left_sublist), len(li)):
        # e.g. len(li) == 5 ==> len(right_sublist) == 5 - 2 == 3, so
        # i == 2 ==> right_sublist[2 - 2] = li[2] 
        # i == 3 ==> right_sublist[3 - 2] = li[3] 
        # i == 4 ==> right_sublist[4 - 2] = li[4] 
        # i == 5 ==> you are done
        right_sublist[i - len(left_sublist)] = li[i] 

    merge_sort(left_sublist)
    merge_sort(right_sublist)
    _merge(li, left_sublist, right_sublist)


def _merge(li, left_sublist, right_sublist):
    """
    Merges two sorted arrays such that the result is another sorted array.

    Example:
    Given [_, _, _, _, _, _], [1, 4, 5], and [0, 2, 3]

    Initialize pointers like so:
    [1, 4, 5]       [0, 2, 3]
     |               |
     l               r

    0 < 1, so put 0 into the temporary array and increment r:
    [0, _, _, _, _, _]
    [1, 4, 5]       [0, 2, 3]
     |                  |
     l                  r          
    
    1 < 3, so put 1 into the temporary array and increment l
    [0, 1, _, _, _, _]
    [1, 4, 5]        [0, 2, 3]
        |                |
        l                r
    
    2 < 4, so put 2 into the temporary array and increment r
    [0, 1, 2, _, _, _]
    [1, 4, 5]        [0, 2, 3]
        |                   |
        l                   r

    3 < 4, so put 3 into the temporary array and increment r
    [0, 1, 2, 3, _, _]
    [1, 4, 5]        [0, 2, 3]
        |                       |
        l                       r

    r out of bounds, so copy the rest of the left subarray into the temporary array
    [0, 1, 2, 3, 4, 5]



    Note that for this implementation, the original list is treated as the temporary array since
    the results will have to be copied into it anyways.
    """
 
    left_pointer = 0
    right_pointer = 0
    list_pointer = 0

    # get the min value of both sublists and append it to the original list
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
    
    # if there are still some elements in the left sublist, just copy them to the list since the sublist is sorted anyways
    while left_pointer < len(left_sublist):
        li[list_pointer] = left_sublist[left_pointer]
        left_pointer += 1
        list_pointer += 1

    # if there are still some elements in the right sublist, just copy them to the list since the sublist is sorted anyways
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