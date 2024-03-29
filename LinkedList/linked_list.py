class LinkedList:
    """ 
    A data structure in which each node contains two items: the data and the next
    node. Keep track of the first node (the "head" of the list), and you can access
    any item in the list.

    Time complexity of searching: O(n)
    Time complexity of inserting/removing first: O(1)
    Time complexity of inserting/removing anywhere else: O(n)

    Strategy:
    Use linear search to access everything. For peeking the recursive version of
    linear searching was used. For modifying the non-recursive version was used out of
    necessity due to the complexity.
    """

    class LLNode:
        """ 
        Internal class to represent a node.
        """
        def __init__(self, item, next):
            self.next = next
            self.item = item


    def __init__(self, first_item=None):
        self.head = None
        if first_item is not None:
            self.add(first_item)
            

    def add_first(self, item):
        """ 
        If the list is empty, set head to a new node. Otherwise set head to a new node
        and set the old head to the next node.
        """
        if self.head is None:
            self.head = self.LLNode(item, None)
        else:
            self.head = self.LLNode(item, self.head)


    def add(self, item, index=0):
        """
        Linearly move to the (i-1)-th node. Then set the i-th node to a new node
        and set the old node to the (i+1)-th node. 
        """
        if self.head is None:
            self.head = self.LLNode(item, None)
            return
        elif index <= 0:
            self.add_first(item)
            return
    
        current_node = self.head
        current_index = 0
        while current_index != index - 1: # Find the node at index i-1
            if current_node.next is None: # End of list was reached before i-th index. Create new node at the end. Return early
                current_node.next = self.LLNode(item, None) 
                return
            else:
                current_index = current_index + 1
                current_node = current_node.next

        if current_node.next is None: # i-th index is the end, so just add a new node
            current_node.next = self.LLNode(item, None) 
        else: # Set the i-th index to a new node and set the old node to the (i+1)-th index
            current_node.next = self.LLNode(item, current_node.next) 


    def add_last(self, item):
        """ 
        If the list is length n, then move to the n-th node. Then add a new node.
        """
        if self.head is None:
            add_first(item)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = self.LLNode(item, None)
    

    def remove_first(self):
        """ 
        If the list is empty, return nothing. Otherwise retrieve head's item and
        let the next node be the new head.
        """
        if self.head is None:
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item


    def remove(self, index=0):
        """
        If the list is empty, return nothing. If the given index is zero, simply remove the
        first element. Otherwise move to the node at index i-1. If the retrieve the item at index
        i and set the (i+1)-th node to the node at index i.
        """
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
            current_node.next = current_node.next.next # Set the node at index i to the node at index i+1
        
        return result

    def remove_last(self):
        """ 
        If the list is empty, then return nothing. If the list only contains one item,
        then return the first item. Otherwise if the list is length n, then go to the 
        (n-1)-th node. Retrieve the item at the n-th node and set the n-th node to None.
        """
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
        

    def clear(self, *, confirm=False):
        """
        Deletes the entire list.
        """
        if confirm:
            self.head = None


    def get(self, index=0):
        """
        Driver for the recursive function.
        """
        return self._get(index, 0, self.head)
    

    def _get(self, index, current_index, current_node):
        """
        Finds the item at the specified index. This is done
        by simply performing linear search on the list.
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
        Finds the first occurance of the specified item. 
        Simply perform linear search on the list.
        """
        if current_node is None:
            return -1
        elif current_node.item == target:
            return current_index
        else:
            return self._find(target, current_index + 1, current_node.next)
    

    def to_list(self):
        """ 
        Iterates through the linked list and retrieves each item as a
        list.
        """
        result = []
        
        current_node = self.head
        while current_node is not None:
            result.append(current_node.item)
            current_node = current_node.next
        
        return result
    

    @staticmethod
    def reverse(linked_list, recursive=True):
        """ 
        Driver for reverse functions.
        """
        if linked_list is None:
            return
        elif linked_list.head is None:
            return
        elif recursive:
            old_head = linked_list.head
            linked_list.head = LinkedList._reverse_rec(linked_list.head)
            old_head.next = None
        else:
            linked_list.head = LinkedList._reverse(linked_list)
    

    @staticmethod
    def _reverse(linked_list):
        """
        Part 1 of a technique used in many technical interview questions.

        Use a two pointer technique with a temporary holder:
        l represents the previous node
        m represents the current node
        r represents a temporary pointer to prevent data loss

        Here is a traceback of the algorithm reversing 1 -> 2 -> 3 -> 4 -> null

       dummy  head
         |    |
        -1 -> 1 -> 2 -> 3 -> 4 -> null
         l    m    r

        m not out of bounds ==> {
            m.next = l
            increment l, m, and r
        }

        -1 <-> 1    2 -> 3 -> 4 -> null
               l    m    r     

        m not out of bounds ==> {
            m.next = l
            increment l, m, and r
        }    

        -1 <-> 1 <- 2    3 -> 4 -> null
                    l    m    r  

        m not out of bounds ==> {
            m.next = l
            increment l, m, and r
        } 
        
        -1 <-> 1 <- 2 <- 3    4 -> null
                         l    m    r   

        m not out of bounds ==> {
            m.next = l
            increment l, m, and r
        } 

       dummy  head
         |     |
        -1 <-> 1 <- 2 <- 3 <- 4    null
                              l    m, r   
        
        m out of bounds ==> {
            head.next = null
            head = l (done in the driver function)
            return
        }

       dummy                head
         |                   |
        -1 -> 1 <- 2 <- 3 <- 4    null
              |              l    m, r
              v
             null
        """

        head = linked_list.head
        dummy = linked_list.LLNode(-1, head)

        l, m, r = dummy, head, head.next

        while m is not None:
            m.next = l
            l = m
            m = r
            r = r.next if r is not None else r
        

        head.next = None
        return l


    
    @staticmethod
    def _reverse_rec(node):
        """
        Part 2 of a technique used in many technical interview questions

        Take advantage of the fact that linked lists are just special cases
        of binary trees by using an algorithm in the style of post-order-traversal.

        Here is a traceback of the algorithm reversing 1 -> 2 -> 3 -> 4 -> null:

        1 -> 2 -> 3 -> 4 -> null
        |
        node

        1 -> 2 -> 3 -> 4 -> null        stack: reverse 1
             |
            node

        1 -> 2 -> 3 -> 4 -> null        stack: reverse 1, reverse 2
                  |
                 node


        1 -> 2 -> 3 -> 4 -> null        stack: reverse 1, reverse 2, reverse 3
                       |
                      node

                     new_head
                        |
        1 -> 2 -> 3 <-> 4    null        stack: reverse 1, reverse 2
                  |
                 node

        1 -> 2 <-> 3 <- 4    null        stack: reverse 1
             |
            node

                     new_head
                        |
        1 <-> 2 <- 3 <- 4    null        
        |
        node


        Refer to the driver to see how to avoid the cycle.
        """
        if node.next is None:
            return node
        
        new_head = LinkedList._reverse_rec(node.next)
        node.next.next = node
        return new_head
        




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

    l.remove(100)
    print("\nNew LL after removing out of bounds: " + str(l.to_list()))

    l.remove(6)
    print("\nNew LL after removing last index: " + str(l.to_list()))

    l.clear(confirm=True)
    print("\nLL after clearing: " + str(l.to_list()))

    l2 = LinkedList()
    for n in [1, 2, 3, 4]:
        l.add(n, n-1)
        l2.add(n, n-1)
    
    print("\nLL before reversing: " + str(l.to_list()))
    LinkedList.reverse(l)
    print("LL after reversing recursively: " + str(l.to_list()))
    LinkedList.reverse(l2, recursive=False)
    print("LL after reversing iteratively: " + str(l2.to_list()))

if __name__ == "__main__":
    main()