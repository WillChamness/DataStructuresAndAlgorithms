class DoublyLinkedList:
    class DLLNode:
        def __init__(self, item, next, previous):
            self.item = item
            self.next = next
            self.previous = previous


    def __init__(self, first_item=None):
        self.head = None
        self.tail = None

        if first_item is not None:
            self.add(first_item)


    def add_first(self, item):
        if self.head is None and self.tail is None:
            self.head = self.DLLNode(item, None, None)
            self.tail = self.head
        else:
            self.head = self.DLLNode(item, self.head, None)
            self.head.next.previous = self.head
        

    def add_last(self, item):
        if self.head is None and self.tail is None:
            self.head = self.DLLNode(item, None, None)
            self.tail = self.head
        else:
            self.tail.next = self.DLLNode(item, None, self.tail)
            self.tail = self.tail.next
    
   
    def get(self, index=0):
        return self._get(index, 0, self.head)


    def _get(self, index, current_index, current_node):
        if current_node is None:
            return None
        elif current_index == index:
            return current_node.item
        else:
            return self._get(index, current_index + 1, current_node.next)


    def find(self, target):
        return self._find(target, 0, self.head)


    def _find(self, target, current_index, current_node):
        if current_node is None:
            return -1
        elif current_node.item == target:
            return current_index
        else:
            return self._find(target, current_index + 1, current_node.next)


    def to_list(self):
        results = []

        current_node = self.head
        while current_node is not None:
            results.append(current_node.item)
            current_node = current_node.next
        
        return results


    def to_list_reverse(self):
        results = []
        current_node = self.tail
        while current_node is not None:
            results.append(current_node.item)
            current_node = current_node.previous

        return results



