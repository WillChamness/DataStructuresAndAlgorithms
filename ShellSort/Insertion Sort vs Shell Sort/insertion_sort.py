def insertion_sort(li, n):
    tmp = 0
    distance = 0
    for i in range(1, n): 
        for j in range(i, 0, -1): 
            distance = j - 1
            if li[j] < li[distance]: 
                tmp = li[j]
                li[j] = li[distance]
                li[distance] = tmp
            else:
                break


def main():
    import random as rd
    import time
    import numpy as np
    a = np.array([rd.randint(0, 1000000) for _ in range(10000)])
    start = time.time()
    b = a[:]
    insertion_sort(b, len(b))
    stop = time.time()

    flag = True
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            flag = False
            break
    
    if flag:
        print("ok")
        print("time:", stop - start)
    else:
        print("something went wrong")


if __name__ == "__main__":
    main()