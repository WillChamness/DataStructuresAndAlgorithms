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

        def left_child_height(self):
            if self.has_left_child():
                return self.left.height
            else:
                return -1

        def right_child_height(self):
            if self.has_right_child():
                return self.right.height
            else:
                return -1

        def max_children_height(self):
            return max(self.left_child_height(), self.right_child_height())

        def update_height(self):
            self.height = self.max_children_height() + 1

        def update_all_heights(self, current_node):
            if current_node is not None:
                if current_node.has_left_child():
                    current_node.update_all_height(current_node.left)
                if current_node.has_right_child():
                    current_node.update_all_height(current_node.right)
                current_node.update_height()
    
    def __init__(self, initial_item=None):
        self.root = None 
        if initial_item is not None:
            self.insert(initial_item)