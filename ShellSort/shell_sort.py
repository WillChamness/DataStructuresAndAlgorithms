def shell_sort(li):
    """
    An optimized insertion sort.

    Time complexity: Ω(n^2)
    Space complexity: O(1)

    Idea: 
    Try to (somehow) get the lesser items closer to the left and the greater items
    closer the right before performing insertion sort. 

    Strategy:
    Let gap == m_1 > 0. Partiion the list such that all items' indeces are congruent to each 
    other (mod m_1). Then perform insertion sort on the sublists. Put the items into the 
    original list in order such that the set of their new indeces is still the same as the set
    of their indeces before partitioning them. Then perform this process for gap == m_(k+1) < m_k 
    for some integer k. Stop if gap < 1.
    

    Some variations of shell sort can reduce the worst case time complexity 
    below n^2. This variation, however, has n^2 as the lower bound (and upper bound)
    time complecity.

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

if __name__ == "__main__":
    main()