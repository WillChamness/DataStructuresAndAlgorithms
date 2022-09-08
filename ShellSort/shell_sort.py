def shell_sort(li):
    """
    An optimized insertion sort.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Idea: 
    Try to (somehow) get the lesser items closer to the left and the greater items
    closer the right before performing insertion sort. 

    Strategy:
    Let gap == m_1 > 0. Partition the list such that all items' indeces are congruent to each 
    other (mod m_1). Then perform insertion sort on the sublists. Put the items into the 
    original list in order such that the set of their new indeces is still the same as the set
    of their indeces before partitioning them. Then perform this process for gap == m_(k+1) < m_k 
    for some integer k. Stop if gap < 1.


    Example:
    Given [3, 5, 1, 7, 2, 6, 4, 0]

    Let gap == 8 // 2 == 4 (half the size of the list).

    To help visualize the next step, I will display the list as such:
    [3, 4, 1, 7,
     2, 6, 4, 0]

    Consider the sublists containing items with indeces 0 and 4, 
    1 and 5, 2 and 6, and 3 and 7: [3, 2], [5, 6], [1, 4], and [7, 0]
    respectively. Perform insertion sort on each of these sublists:
    [2, 3], [5, 6], [1, 4], and [0, 7]. Take the first item of every
    sublist from left to right: [3, 5, 1, 7]. Now append the second
    item of the sublists from left to right: [3, 5, 1, 7, 2, 6, 4, 0].
    Let this new list represent the original. Now let gap == 4 // 2 == 2.

    To help visualize the next step, I will display the list as such:
    [3, 5,
     1, 7,
     2, 6,
     4, 0]
    Conisder the sublists containing items with indeces 0, 2, 4, 6
    and 1, 3, 5, 7: [3, 1, 2, 4] and [5, 7, 6, 0] respectively. Perform 
    insertion sort on each of these sublists: [1, 2, 3, 4] and [0, 5, 6, 7].
    Now take the first item of every sublist from left to right:
    [1, 0]. Now append the second item of the sublists from left to right:
    [1, 0, 2, 5]. Now append the third item of the sublists from left to 
    right: [1, 0, 2, 5, 3, 6]. Now append the fourth item of the sublists
    from left to right: [1, 0, 2, 5, 3, 6]. Let this list represent the 
    original. Now let gap == 2 // 2 == 1.

    Side note: 
    If gap == 1, then you are simply performing insertion sort on the entire list.
    Notice how the lesser numbers have moved closer to the left and the greater 
    numbers have moved closer to the right. We have achived our goal in this case.

    To help visualize the next step, I will display the list as such:
    [1,
     0,
     2, 
     5, 
     3, 
     6, 
     4, 
     7]. 
    Consider the sublist with indeces 0, 1, 2, 3, 4, 5, 6, 7:
    [1, 0, 2, 5, 3, 6, 4, 7]. Perform insertion sort on this sublist:
    [0, 1, 2, 3, 4, 5, 6, 7]. Now take the first item of the sublist:
    [0]. Now append the second item of the sublist: [0, 1]. Now append
    the third item of the sublist: [0, 1, 2]. Continue this until you 
    reach the last index: [0, 1, 2, 3, 4, 5, 6, 7]. Let this list
    represent the original. Now let gap == 1 // 2 == 0.

    gap < 1. Therefore the list is now sorted.


    Some variations of shell sort can reduce the worst case time complexity 
    below n^2 (see shell_sort_optimized.py). As a result, shell sort is *technically*
    an optimization to insertion sort. This variation, however, has the same time 
    complexity as insertion sort, namely O(n^2). Furthermore, this variation has a 
    higher cache miss rate. Consequently, this variation is actually worse than 
    insertion sort despite the fact that they have the same time complexity.

    Compare to insertion sort to see similarities.
    """

    def swap(li, i1, i2):
        temp = li[i1]
        li[i1] = li[i2]
        li[i2] = temp

    gap = len(li) // 2 # gap == 1 ==> perform insertion sort
    while gap > 0:
        # consider the sublists containing indeces ...
        for i in range(gap, len(li)): 
            # perform insertion sort on all sublists simultaneously
            for j in range(i, 0, -gap): 
                if j - gap >= 0 and li[j] < li[j - gap]: # don't want to swap with negative indeces
                    swap(li, j, j - gap) 
                else:
                    break
        gap //= 2


def main():
    import random as r 
    l = []

    for i in range(10):
        l.append(r.randint(0,100))
    
    print(f"Before: {l}")
    shell_sort(l)
    print(f"After: {l}")

    l = []
    for i in range(11):
        l.append(r.randint(0,100))
    
    print(f"Before: {l}")
    shell_sort(l)
    print(f"After: {l}")

if __name__ == "__main__":
    main()