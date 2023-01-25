from bst import BST
def tree_sort(li):
    """ 
    Worst case time complexity: O(n^2) 
    Average time complexity: O(n*log(n))
    Space complexity: O(n)

    Worst case time complexity can be improved to O(n*log(n)) with
    self-balancing trees. Uses in-order traversal to sort (see BST data structure).
    """

    t = BST()
    for item in li:
        t.insert(item)

    new_li = t.in_order_traversal()
    return new_li


def main():
    import random as r 
    l = []
    for i in range(10):
        l.append(r.randint(0,100))

    print(f"Before: {l}")

    l = tree_sort(l)

    print(f"After: {l}")

if __name__ == "__main__":
    main()