from max_heap import MaxHeap

def max(li, i, j):
    if li[i] > li[j]: return i
    else: return j


def swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp


def percolate_down(heap, index, size):
    left = 2*index + 1
    right = 2*index + 2

    if left >= size: # size represents out of bounds, thus no left child
        return
    if right >= size: # no right child
        if index != max(heap, index, left):
            swap(heap, index, left)
        return
    
    max_index = max(heap, index, max(heap, left, right))
    if left == max_index:
        swap(heap, index, left)
        percolate_down(heap, left, size)
    elif right == max_index:
        swap(heap, index, right)
        percolate_down(heap, right, size)
    

def heap_sort(li):
    """ 
    Uses concepts from max heaps to sort a list.

    Could use a min heap and remove each item into a new list instead, but 
    that would cause the space complexity to increase to O(n).
    """
    MaxHeap.heapify(li)
    size = len(li)
    for n in range(len(li)):
        swap(li, 0, size - 1) # "remove" max
        size -= 1
        percolate_down(li, 0, size)
    

def main():
    import random as r 
    l = []
    for i in range(10):
        l.append(r.randint(0, 100))
    print(f"Before: {l}")

    heap_sort(l)
    print(f"After: {l}")

if __name__ == "__main__":
    main()