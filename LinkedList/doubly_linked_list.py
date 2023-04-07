class DoublyLinkedList:
    """ 
    Doubly linked list. Very similar to a singly linked list.
    See linked_list.py for more details.

    Time complexity of searching: O(n)
    Time complexity of inserting/removing first: O(1)
    Time complexity of inserting/removing last: O(1)
    Time complexity of inserting/removing anywhere else: O(n)
    """    
    class DLLNode:
        """
        Internal class to represent a node.
        """
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
        """ 
        Adds a new node to the head of the list.
        """
        if self.head is None and self.tail is None:
            self.head = self.DLLNode(item, None, None)
            self.tail = self.head
        else:
            self.head = self.DLLNode(item, self.head, None)
            self.head.next.previous = self.head


    def add(self, item, index=0):
        """ 
        Adds a new node at the specified index.
        """
        if self.head is None and self.tail is None:
            self.head = self.DLLNode(item, None, None)
            self.tail = self.head
            return
        elif index <= 0:
            self.add_first(item)
            return

        current_node = self.head
        current_index = 0
        while current_index != index - 1:
            if current_node.next is None:
                self.add_last(item)
                return
            else:
                current_index = current_index + 1
                current_node = current_node.next
        
        if current_node.next is None:
            self.add_last(item)
        else:
            current_node.next = self.DLLNode(item, current_node.next, current_node)
            current_node.next.next.previous = current_node.next
        

    def add_last(self, item):
        """ 
        Adds a new node to the tail of the list.
        """
        if self.head is None and self.tail is None:
            self.head = self.DLLNode(item, None, None)
            self.tail = self.head
        else:
            self.tail.next = self.DLLNode(item, None, self.tail)
            self.tail = self.tail.next
    

    def remove_first(self):
        """ 
        Removes the current head of the list.
        """
        if self.head is None and self.tail is None:
            return None
        elif self.head.next is None:
            item = self.head.item
            self.head = None
            self.tail = None
            return item
        else:
            item = self.head.item
            self.head = self.head.next
            self.head.previous = None
            return item


    def remove(self, index=0):
        """ 
        Removes the node at the specified index.
        """
        if self.head is None and self.tail is None:
            return None
        elif index <= 0:
            return self.remove_first()
        
        current_index = 0
        current_node = self.head
        while current_index != index - 1:
            if current_node.next is None:
                return None
            else:
                current_index = current_index + 1
                current_node = current_node.next
        
        result = None
        if current_index != index - 1:
            result = current_node.next.item 
            current_node.next = current_node.next.next
            current_node.next.previous = current_node
        else:
            result = self.remove_last()

        return result
    

    def remove_last(self):
        """ 
        Removes the node at the tail of the list.
        """
        if self.head is None and self.tail is None:
            return None
        elif self.head is None: # sanity check
            return self.remove_first()
        
        item = self.tail.item
        self.tail = self.tail.previous
        self.tail.next = None
        return item
    
    
    def clear(self, *, confirm=False):
        """ 
        Destroys the entire list.
        """
        if confirm:
            self.head = None
            self.tail = None

    
    def get(self, index=0):
        """ 
        Driver for the recursive method.
        """
        return self._get(index, 0, self.head)


    def _get(self, index, current_index, current_node):
        """ 
        Retrieves the item at the specified index.
        """
        if current_node is None:
            return None
        elif current_index == index:
            return current_node.item
        else:
            return self._get(index, current_index + 1, current_node.next)


    def find(self, target):
        """ 
        Driver for the recursive method.
        """
        return self._find(target, 0, self.head)


    def _find(self, target, current_index, current_node):
        """ 
        Returns the index of the first occurrence of the specified item.
        """
        if current_node is None:
            return -1
        elif current_node.item == target:
            return current_index
        else:
            return self._find(target, current_index + 1, current_node.next)


    def to_list(self):
        """ 
        Iterates through the linked list in order.
        """
        results = []

        current_node = self.head
        while current_node is not None:
            results.append(current_node.item)
            current_node = current_node.next
        
        return results

    def to_list_reverse(self):
        """ 
        Iterates through the linked list backwards.
        """
        results = []
        current_node = self.tail
        while current_node is not None:
            results.append(current_node.item)
            current_node = current_node.previous

        return results



def main():
    l = DoublyLinkedList()
    before = []
    for i in range(10):
        before.append(i)
    print("Before: " + str(before))

    for n in before:
        l.add(n)
    
    after = []
    while l.get() is not None:
        after.append(l.remove())
    print("After: " + str(after))

    before = "abcdefg"
    print("\nBefore: " + before)
    for c in before:
        l.add(c)
    
    print("After: " + str(l.to_list()))
    print("In reverse: " + str(l.to_list_reverse()))

    print("\nItem at index 3: " + l.get(3))
    print("'b' is at index: " + str(l.find('b')))


    l.add("x", 4)
    l.add("y", 4)
    l.add("z", 100)
    print("\n\nNew LL after adding: " + str(l.to_list()))
    print("In reverse: " + str(l.to_list_reverse()))

    l.add_first("1")
    l.add_last("10")
    print("\nNew LL after adding first and last: " + str(l.to_list()))
    print("In reverse: " + str(l.to_list_reverse()))

    l.remove(l.find("y"))
    l.remove(l.find("a"))
    l.remove(l.find("f"))
    print("\nNew LL after removing: " + str(l.to_list()))
    print("In reverse: " + str(l.to_list_reverse()))

    l.remove_first()
    l.remove_last()
    print("\nNew LL after removing first and last: " + str(l.to_list()))
    print("In reverse: " + str(l.to_list_reverse()))

    l.remove(100)
    print("\nNew LL after removing out of bounds: " + str(l.to_list()))
    print("In reverse: " + str(l.to_list_reverse()))

    l.remove(6)
    print("\nLL after removing last index: " + str(l.to_list()))
    print("In reverse: " + str(l.to_list_reverse()))

    l.clear(confirm=True)
    print("\nLL after clearing: " + str(l.to_list()))



if __name__ == "__main__":
    main()