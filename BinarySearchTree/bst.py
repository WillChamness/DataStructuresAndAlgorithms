class BST:
    """ 
    A data structure in which each node contains three items: the data and two 
    child nodes. Furthermore, each node is bound by a certain rule: all items
    less than the node's value can be accessed from the node's left child (if 
    it exists), and items greater than the node's value can be accessed from the
    node's right child (if it exists). Duplicate values are discarded.
    """

    class TreeNode:
        """
        Represents the nodes.
        """
        def __init__(self, item, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right


    def __init__(self, first_item=None):
        self.root = None
        if first_item is not None:
            self.insert(first_item)


    def insert(self, item):
        """ 
        Driver for recursive function _insert()
        """
        if self.root is None:
            self.root = self.TreeNode(item)
        else:
            self._insert(item, self.root)


    def _insert(self, item, current_node):
        """ 
        Recursively descends down the tree to insert a new node.
        If the item is less than the current node's item, the item
        must be to the left of the current node. Likewise, if the
        item is greater than the current node's item, the item
        must be to the right of the current node.

        Time complexity: O(log(n))
        Space complexity: O(1)
        """
        if item < current_node.item:
            if current_node.left is None:
                current_node.left = self.TreeNode(item)
            else:
                self._insert(item, current_node.left)
        elif item > current_node.item:
            if current_node.right is None:
                current_node.right = self.TreeNode(item)
            else:
                self._insert(item, current_node.right)


    def remove(self, item):
        """
        Driver for recursive function _remove()
        """
        if self.root is None:
            return
        else:
            self.root = self._remove(item, self.root)


    def _remove(self, item, current_node):
        """
        Recursively descends down the tree to delete the node. When it reaches
        the target node (assuming it exists), swap the item with another node's
        and delete the other node.

        Time complexity: O(log(n))
        Space complexity: O(1)
        """
        if current_node is None:
            return None

        if item < current_node.item:
            current_node.left = self._remove(item, current_node.left)
            return current_node

        elif item > current_node.item:
            current_node.right = self._remove(item, current_node.right)
            return current_node

        else:
            if (current_node.left is not None) and (current_node.right is not None):  # case where node has two children
                # Go right then all the way left. You could also go left then all the way right instead.
                # This will guarantee a node that will not violate BST requirements
                parent = current_node.right
                child = parent.left
                while child is not None:
                    parent = child
                    child = child.left
                current_node.item = parent.item  # change node's value to the pointer's value
                current_node.right = self._remove(current_node.item, current_node.right)
                return current_node

            elif (current_node.left is not None) and (current_node.right is None):  # case where node has one child
                current_node.item = current_node.left.item
                current_node.left = self._remove(current_node.item, current_node.left)
                return current_node

            elif (current_node.right is not None) and (current_node.left is None):  # case where node has one child
                current_node.item = current_node.right.item
                current_node.right = self._remove(current_node.item, current_node.right)
                return current_node
                
            else:  # case where node has no children
                return None 


    def search(self, target):
        """ 
        Driver for recursive function _search()
        """
        if self.root is None:
            return False
        else:
            return self._search(target, self.root)
    
    
    def _search(self, target, current_node):
        """ 
        Traverse the tree until the target is found or until
        a null node is reached. 

        Time complexity: O(log(n))
        Space complexity: O(1)
        """
        if current_node is None:
            return False
        if target == current_node.item:
            return True
        elif target < current_node.item:
            return self._search(target, current_node.left)
        else:
            return self._search(target, current_node.right)


    def depth_first_search(self, traversal=0):
        """ 
        A way to visit every node once. There are three kinds of 
        depth first search:

        - Pre-order traversal
        - In-order traversal
        - Post-order traversal

        Regardless, the time complexity is O(n). Furthermore,
        this implementation copies the nodes into a new list
        to visualize the results, so the space complexity is 
        O(n). However, you can process each node however you
        want.
        """
        results = []
        if traversal < 0:
            self._pre_order_traversal(self.root, results)
        elif traversal > 0:
            self._post_order_traversal(self.root, results)
        else:
            self._in_order_traversal(self.root, results)
        return results


    def _pre_order_traversal(self, current_node, li):
        """ 
        Process the node, then process the left and right children.
        For example, given this tree:

                    100
                   /   \
                  50    200
                 / \    / 
                25  75 150
                        \
                         175

        You would process the nodes in this order:
        100, 50, 25, 75, 200, 150, 175
        """
        if current_node is not None:
            li.append(current_node.item)
            self._pre_order_traversal(current_node.left, li)
            self._pre_order_traversal(current_node.right, li)


    def _in_order_traversal(self, current_node, li):
        """
        Process the left child, then the node, then the right child.
        For example, given this tree:

                    100
                   /   \
                  50    200
                 / \    / 
                25  75 150
                        \
                         175

        You would process the nodes in this order:
        25, 50, 75, 100, 150, 175, 200

        Notably, this returns an array of all items in sorted order.
        See TreeSort for more details.
        """
        if current_node is not None:
            self._in_order_traversal(current_node.left, li)
            li.append(current_node.item)
            self._in_order_traversal(current_node.right, li)


    def _post_order_traversal(self, current_node, li):
        """ 
        Process the left and right children, then the node.
        For example, given this tree:

                    100
                   /   \
                  50    200
                 / \    / 
                25  75 150
                        \
                         175

        You would process the nodes in this order:
        25, 75, 50, 175, 150, 200, 100
        """
        if current_node is not None:
            self._post_order_traversal(current_node.left, li)
            self._post_order_traversal(current_node.right, li)
            li.append(current_node.item)


    def breadth_first_search(self):
        """ 
        A way to visit every node once. Process the nodes from
        top to bottom. For example, given the tree:

                    100
                   /   \
                  50    200
                 / \    / 
                25  75 150
                        \
                         175

        You would process the nodes in this order:
        100, 50, 200, 25, 75, 150, 175

        The code follows this procedure:
        - initialize a queue to contain the root
        - while you still have nodes to process, process the node
          at the front of the queue and add the node's children

        Time complexity: O(n)
        Space complexity: O(n)
        """
        if self.root is None:
            return []
            
        from queue_list import QueueList
        import sys
        results = []
        q = QueueList(sys.maxsize)
        q.enqueue(self.root)

        while not q.is_empty():
            parent = q.dequeue()
            results.append(parent.item)
            if parent.left is not None: q.enqueue(parent.left)
            if parent.right is not None: q.enqueue(parent.right)

        return results

    
    @staticmethod
    def invert(binary_search_tree):
        """
        Driver for recursive function.
        """
        if binary_search_tree is None:
            return
        else:
            BST._invert(binary_search_tree.root)


    @staticmethod
    def _invert(node):
        """
        A technique for many technical interview questions. Use a 
        post-order-traversal algorithm to invert.
        """
        if node is None:
            return
        
        # process the children
        BST._invert(node.left)
        BST._invert(node.right)

        # then process the current node
        l = node.left
        r = node.right

        node.left = r
        node.right = l


def main():
    import random as r 
    t = BST()

    before = []
    for _ in range(10):
        before.append(r.randint(0, 100))
    print(f"Before: {before}")

    for item in before:
        t.insert(item) # reminder: tree will discard duplicates

    print(f"Pre-order traversal: {t.depth_first_search(-1)}")
    print(f"In-order traversal: {t.depth_first_search()}")
    print(f"Post-order traversal: {t.depth_first_search(1)}")

    print(f"Breadth-first search: {t.breadth_first_search()}")

    t.insert(100)
    print("Added 100")
    print(f"Search results for 100: {t.search(100)}")
    print(f"Search results for 1000: {t.search(1000)}")

    t.remove(100) # has no children
    print(f"breadth first search: {t.depth_first_search()} (after removing 100)")
    t.remove(-1)
    print(f"breadth first search: {t.depth_first_search()} (after removing -1)")

    t = BST()
    print("before:", [100, 50, 200, 25, 75, 150])
    for n in [100, 50, 200, 25, 75, 150]:
        t.insert(n)

    t.remove(200) # has one child
    print("Removing 200 from before:", t.breadth_first_search())
    t = BST()
    for n in [100, 50, 200, 25, 75, 150]:
        t.insert(n)
    t.remove(50) # has two children
    print("Removing 50 from before:", t.breadth_first_search())

    t = BST()
    for n in [100, 50, 200, 25, 75]:
        t.insert(n)
    print("BST before inverting:", t.breadth_first_search())
    BST.invert(t)
    print("BST after inverting:", t.breadth_first_search())



if __name__ == "__main__":
    main()