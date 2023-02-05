class AVLTree:
    class TreeNode:
        def __init__(self, item, left=None, right=None, height=0):
            self.item = item
            self.left = left
            self.right = right
            self.height = height

        def is_balanced(self):
            return abs(self.left_child_height() - self.right_child_height()) < 2

        def has_left_child(self):
            return self.left is not None
        
        def has_right_child(self):
            return self.right is not None