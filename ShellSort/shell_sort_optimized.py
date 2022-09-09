import math

def update_gap(k, sequence):
    return sequence(k)

def swap(li, index1, index2):
    temp = li[index1]
    li[index2] = li[index1]
    li[index1] = temp

def shell_sort_hibbard(li):
    """ 
    Define the gap as such:
    g_k == 2^k - 1 for some positive integer k

    Time complexity: O(n^(3/2))
    Space complexirt: O(1)
    """

    n = len(li) # store length for optimization purposes
    k = int(math.log(n, 2)) # initializing k like this will guarentee a gap <= n
    SEQUENCE = lambda k : 2**k - 1
    gap = update_gap(k, SEQUENCE)

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if j >= gap and li[j] < li[j - gap]:
                    swap(li, j, j - gap)
                else:
                    break
        k -= 1
        gap = update_gap(k, SEQUENCE)
    
