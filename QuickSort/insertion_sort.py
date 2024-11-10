def insertion_sort(li):    
    for i in range(1, len(li)): 
        for j in range(i, 0, -1):
            if li[j] < li[j-1]: 
                _swap(li, j, j-1)
            else:
                break

def partial_insertion_sort(li, lo, hi):
    for i in range(1 + lo, 1 + hi):
        for j in range(i, lo, -1):
            if li[j] < li[j-1]:
                _swap(li, j, j-1)
            else:
                break
    

def _swap(li, index1, index2):
        temp = li[index1]
        li[index1] = li[index2]
        li[index2] = temp