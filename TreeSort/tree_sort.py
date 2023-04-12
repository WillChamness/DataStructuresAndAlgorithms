from bst import BST


def tree_sort(li):
    """ 
    Worst case time complexity: O(n^2) 
    Average time complexity: O(n*log(n))
    Space complexity: O(n)

    The worst case occurs when the tree resembles a linked list. Adding n elements
    to the end of such a tree is has a time complexity of O(n^2).

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
    l = list([r.randint(1, 100) for _ in range(10)])  # n is even

    print(f"Before: {l}")
    l = tree_sort(l)
    print(f"After: {l}")

    l = list([r.randint(1, 100) for _ in range(11)])  # n is odd
    print(f"Before: {l}")
    l = tree_sort(l)
    print(f"After: {l}")


if __name__ == "__main__":
    main()
