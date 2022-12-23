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