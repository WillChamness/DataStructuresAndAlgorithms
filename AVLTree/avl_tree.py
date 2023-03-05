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
                return self._right_rotate(current_node)
            else: # otherwise must be LR case
                current_node.left = self._left_rotate(current_node.left)
                return self._right_rotate(current_node)
        else: # imbalance caused by right child
            if current_node.right.left_child_height() > current_node.right.right_child_height(): # RL case
                current_node.right = self._right_rotate(current_node.right)
                return self._left_rotate(current_node)
            else: # otherwise must be RR case
                return self._left_rotate(current_node)


    def _left_rotate(self, current_node):
        new_parent = current_node.right 
        rightleft_backup = current_node.right.left 

        new_parent.left = current_node
        current_node.right = rightleft_backup

        current_node.update_height()
        new_parent.update_height()

        return new_root


    def _right_rotate(self, current_node):
        new_parent = current_node.left 
        leftright_backup = current_node.left.right 

        new_parent.right = current_node
        current_node.left = leftright_backup

        current_node.update_height()
        new_parent.update_height()

        return new_parent

    
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
            if current_node.has_left_child() and current_node.has_right_child():
                pointer = current_node.right
                while pointer.left is not None:
                    pointer = pointer.left
                current_node.item = pointer.item 
                pointer = None 
            elif current_node.has_left_child() and not current_node.has_right_child(): 
                current_node = current_node.left
            elif not current_node.has_left_child() and current_node.has_right_child(): 
                current_node = current_node.right
            else: 
                current_node = None

        if current_node is not None:
            current_node = self._rebalance(current_node)

    
    def search(self, item):
        if self.root is None:
            return False
        else:
            return self._search(self, item, self.root)
    

    def _search(self, item, current_node):
        if current_node is None:
            return False
        if item == current_node.item:
            return True
        elif item < current_node.item:
            return self._search(item, current_node.left)
        else:
            return self._search(item, current_node.right)

    
    def depth_first_search(self, traversal=0):
        results = []
        if traversal < 0:
            self._pre_order_traversal(self.root, results)
        elif traversal > 0:
            self._pre_order_traversal(self.root, results)
        else:
            self._in_order_traversal(self.root, results)
        return results

    
    def _pre_order_traversal(self, current_node, li):
        if current_node is not None:
            li.append(current_node.item)
            self._pre_order_traversal(current_node.left, li)
            self._pre_order_traversal(current_node.right, li)


    def _in_order_traversal(self, current_node, li):
        if current_node is not None:
            self._in_order_traversal(current_node.left, li)
            li.append(current_node.item)
            self._in_order_traversal(current_node.right, li)
    

    def _post_order_traversal(self, current_node, li):
        if current_node is not None:
            self._post_order_traversal(current_node.left, li)
            self._post_order_traversal(current_node.right, li)
            li.append(current_node.item)

    
    def breadth_first_search(self):
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