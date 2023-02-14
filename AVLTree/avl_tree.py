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

    def insert(self, item):
        if self.root is None:
            self.root = self.TreeNode(item)
        else:
            self.root = self._insert(item, self.root)

    def _insert(self, item, current_node):
        if item < current_node.item:
            if current_node.has_left_child():
                self._insert(item, current_node.left)
            else:
                current_node.left = self.TreeNode(item)
        elif item > current_node.item:
            if current_node.has_right_child():
                self._insert(item, current_node.right)
            else:
                current_node.right = self.TreeNode(item)

        current_node = self._rebalance(current_node) # rebalance from the bottom up
        return current_node

    def _rebalance(self, current_node):
        if current_node.is_balanced(): 
            return current_node

        if current_node.left_child_height() > current_node.right_child_height(): # imbalance caused by left child
            if current_node.left.left_child_height() > current_node.left.right_child_height(): # LL case
                return self.right_rotate(current_node)
            else: # otherwise must be LR case
                current_node.left = self.left_rotate(current_node.left)
                return self.right_rotate(current_node)
        else: # imbalance caused by right child
            if current_node.right.left_child_height() > current_node.right.right_child_height(): # RL case
                current_node.right = self.right_rotate(current_node.right)
                return self.left_rotate(current_node)
            else: # otherwise must be RR case
                return self.left_rotate(current_node)