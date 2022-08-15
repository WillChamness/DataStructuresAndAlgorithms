class LinkedList:
    class LLNode:
        def __init__(self, item, next):
            self.next = next
            self.item = item


    def __init__(self, first_item=None):
        self.head = None
        if first_item is not None:
            self.add(first_item)
            

    def add_first(self, item):
        if self.head is None:
            self.head = self.LLNode(item, None)
        else:
            self.head = self.LLNode(item, self.head)


    def add(self, item, index=0):
        if self.head is None:
            self.head = self.LLNode(item, None)
            return
        elif index <= 0:
            self.add_first(item)
            return
    
        current_node = self.head
        current_index = 0
        while current_index != index - 1: # Find the node at index i-1
            if current_node.next is None:
                current_node.next = self.LLNode(item, None) # End of list was reached before i-th index. Create new node at the end. Return early
                return
            else:
                current_index = current_index + 1
                current_node = current_node.next

        if current_node.next is None: # i-th index is the end, so just add a new node
            current_node.next = self.LLNoe(item, None) 
        else: # Set the i-th index to a new node and set the old node to the (i+1)-th index
            current_node.next = self.LLNode(item, current_node.next) 


    def add_last(self, item):
        if self.head is None:
            add_first(item)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = self.LLNode(item, None)
    

    def remove_first(self):
        if self.head is None:
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item


    def remove(self, index=0):
        if self.head is None:
            return None
        elif index <= 0:
            return self.remove_first()
        
        current_index = 0
        current_node = self.head
        while current_index != index - 1: # find the node at index i-1
            if current_node.next == None: # end of list reached before getting to node i. Return early
                return None
            else:
                current_index = current_index + 1
                current_node = current_node.next

        result = None
        if current_node.next is not None: # node at index i is not the end of the list
            result = current_node.next.item
            current_node.next = current_node.next.next
        
        return result

    def remove_last(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            return remove_first()
        
        current_node = self.head
        while current_node.next.next is not None: # Go to the 2nd to last node
            current_node = current_node.next
        
        item = current_node.next.item # retrieve the item
        current_node.next = None # remove the last node
        return item
        

    def clear(self):
        self.head = None


    def get(self, index=0):
        return self.__get__(index, 0, self.head)
    

    def __get__(self, index, current_index, current_node):
        if current_node is None:
            return None
        elif current_index == index:
            return current_node.item 
        else:
            return self.__get__(index, current_index + 1, current_node.next)


    def find(self, target):
        return self.__find__(target, 0, self.head)


    def __find__(self, target, current_index, current_node):
        if current_node is None:
            return -1
        elif current_node.item == target:
            return current_index
        else:
            return self.__find__(target, current_index + 1, current_node.next)
    

    def to_list(self):
        result = []
        
        current_node = self.head
        while current_node is not None:
            result.append(current_node.item)
            current_node = current_node.next
        
        return result


def main():
    l = LinkedList()
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

    print("\nItem at index 3: " + l.get(3))
    print("'b' is at index: " + str(l.find('b')))


    l.add("x", 4)
    l.add("y", 4)
    l.add("z", 100)
    print("\n\nNew LL after adding: " + str(l.to_list()))

    l.add_first("1")
    l.add_last("10")
    print("\nNew LL after adding first and last: " + str(l.to_list()))

    l.remove(l.find("y"))
    l.remove(l.find("a"))
    l.remove(l.find("f"))
    print("\nNew LL after removing: " + str(l.to_list()))

    l.remove_first()
    l.remove_last()
    print("\nNew LL after removing first and last: " + str(l.to_list()))

    l.clear()
    print("\nLL after clearing: " + str(l.to_list()))

if __name__ == "__main__":
    main()