# Information about time complexities and authors taken from here:
# https://en.wikipedia.org/wiki/Shellsort

import math

def swap(li, index1, index2):
    temp = li[index1]
    li[index1] = li[index2]
    li[index2] = temp

def shell_sort_hibbard(li):
    """ 
    Define the gap as such:
    g_k == 2^k - 1 > 0 for some positive integer k

    Time complexity: O(n^(3/2))
    Space complexity: O(1)
    """

    n = len(li) # store length for optimization purposes
    k = int(math.log(n, 2)) # initializing k like this will guarentee a gap <= n
    SEQUENCE = lambda k : 2**k - 1
    gap = SEQUENCE(k)

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if j >= gap and li[j] < li[j - gap]:
                    swap(li, j, j - gap)
                else:
                    break
        k -= 1
        gap = SEQUENCE(k)


def shell_sort_sedgewick_1982(li):
    """ 
    Define gap as a piecewise function:
    g_k = { 1, k = 0
          { (2^k)^2 + (3/2)(2^k) + 1 = 4^k + 3(2)^k-1 + 1, k > 0
    """
    n = len(li)
    k = int(math.log(math.sqrt(n), 2))

    SEQUENCE = lambda k : 4**k + 3*2**(k-1) + 1 if k >= 1 else (1 if k == 0 else 0)
    gap = SEQUENCE(k)

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if j >= gap and li[j] < li[j - gap]:
                    swap(li, j, j - gap)
                else:
                    break
        k -= 1
        gap = SEQUENCE(k)


def shell_sort_ciura(li):
    """ 
    Gap experimentally derived. Formula unknown as of 9/9/2022.
    Gap is an element of [1, 4, 10, 23, 57, 132, 301, 701]

    Time complexity: unknown as of 9/19/2022
    Space complexity: O(1)
    """
    n = len(li)
    k = 7 # last index of list below
    SEQUENCE = lambda k : [1, 4, 10, 23, 57, 132, 301, 701][k] 
    gap = SEQUENCE(k)

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if j >= gap and li[j] < li[j - gap]:
                    swap(li, j, j - gap)
                else:
                    break
        k -= 1
        gap = SEQUENCE(k)


def main():
    import random as rd 
    l = []
    for i in range(3):
        temp = []
        for j in range(10):
            temp.append(rd.randint(0, 100))
        l.append(temp)
        
    print("Before (hibbard):", l[0])
    shell_sort_hibbard(l[0])
    print("After (hibbard):", l[0])

    print("\nBefore (sedgewick):", l[1])
    shell_sort_sedgewick_1982(l[1])
    print("After (sedgewick):", l[1])

    print("\nBefore (cuira):", l[2])
    shell_sort_ciura(l[2])
    print("After (ciura):", l[2])

 

if __name__ == "__main__":
    main()