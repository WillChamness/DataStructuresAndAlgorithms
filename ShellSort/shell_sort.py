def shell_sort(li):
    """
    An optimized insertion sort.

    Time complexity: Ω(n^2)
    Space complexity: O(1)


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