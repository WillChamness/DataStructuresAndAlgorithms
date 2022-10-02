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
    k = int(math.log(n, 2)) # initializing k like this will guarentee a gap < n
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

    Time complexity: O(n^4/3)
    Space complexity: O(1)
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
    k = 8 # last index of list below
    SEQUENCE = lambda k : [0, 1, 4, 10, 23, 57, 132, 301, 701][k] # append 0 to front of list to exit loop when done
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


def shell_sort_generic(li: list, sequence: type(lambda x : 1), initial_k: int, k_step: type(lambda x : 1)=lambda k : k-1):
    """ 
    Generic shell sort function. Sequence is a function of k, and k will increment/decrement based on k_step. Gap must be
    an integer, and for the first iteration, gap must be greater than or equal to 1.
    """ 
    if type(sequence) is not type(lambda x : 1):
        raise TypeError("Sequence not a function")
    k = initial_k
    n = len(li)
    gap = sequence(k)
    if type(gap) is not int:
        raise TypeError("Bad sequence")
    if gap < 1:
        raise ValueError("Bad initial k")

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if j >= gap and li[j] < li[j - gap]:
                    swap(li, j, j - gap)
                else:
                    break 
        k = k_step(k)
        gap = sequence(k)
        if type(gap) is not int:
            raise TypeError("Bad sequence or k_step")



def main():
    import random as rd 
    l = []
    for i in range(5):
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

    print("\nBefore (ciura):", l[2])
    shell_sort_ciura(l[2])
    print("After (ciura):", l[2])

    print("\nBefore (generic):", l[3])
    # original shell sort - initial k negative as workaround since k decrements
    shell_sort_generic(l[3], lambda k : int(len(l[3]) / 2**-k), -1)
    print("After (generic):", l[3])

    print("\nBefore (generic):", l[4])
    # same as before, but the sequence is expressed in a more natural function
    shell_sort_generic(l[4], lambda k : int(len(l[4]) / 2**k), 1, lambda k : k+1)
    print("After (generic):", l[4])
 
 

if __name__ == "__main__":
    main()