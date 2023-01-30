class BST:
    class Node:
        def __init__(self, item, l=None, r=None):
            self.item = item
            self.l = l
            self.r = r

    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = self.Node(item)
        else:
            self._insert(item, self.root)


    def _insert(self, item, node):
        if item < node.item:
            if node.l is None:
                node.l = self.Node(item)
            else:
                self._insert(item, node.l)
        else: # allow duplicate nodes
            if node.r is None:
                node.r = self.Node(item)
            else:
                self._insert(item, node.r)

    def in_order_traversal(self):
        results = []
        self._iot(self.root, results)
        return results

    def _iot(self, node, li):
        if node is not None:
            self._iot(node.l, li)
            li.append(node.item)
            self._iot(node.r, li)
