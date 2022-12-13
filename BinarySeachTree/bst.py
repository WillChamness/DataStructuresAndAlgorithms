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