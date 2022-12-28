class BST:
    class TreeNode:
        def __init__(self, item, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right

    def __init__(self, first_item=None):
        self.root = None
        if first_item is not None:
            self.insert(first_item)

    def insert(self, item):
        if self.root is None:
            self.root = self.TreeNode(item)
        else:
            self._insert(item, self.root)

    def _insert(self, item, current_node):
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
        if self.root is None:
            return None
        else:
            return self._remove(item, self.root)

    def _remove(self, item, current_node):
        if item < current_node.item:
            if current_node.left is not None:
                self._remove(item, current_node.left)
        elif item > current_node.item:
            if current_node.right is not None:
                self._remove(item, current_node.right)
        else: 
            if current_node.left is not None and current_node.right is not None: # case where node has two children
                # Go right then all the way left. You could also go left then all the way right instead. 
                # This will guarentee an item less than the current node
                pointer = current_node.right
                while pointer.left is not None:
                    pointer = pointer.left
                current_node.item = pointer.item # change node's value to the pointer's value
                pointer = None # remove the pointer
            elif current_node.left is not None and current_node.right is None: # case where node has one child
                current_node = current_node.left
            elif current_node.right is not None and current_node.left is None: # case where node has one child
                current_node = current_node.right
            else: # case where node has no children
                current_node = None

    def depth_first_search(self, traversal=0):
        results = []
        if traversal < 0:
            self._pre_order_traversal(self.root, results)
        elif traversal > 0:
            self._post_order_traversal(self.root, results)
        else:
            self._in_order_traversal(self.root, results)
        return results