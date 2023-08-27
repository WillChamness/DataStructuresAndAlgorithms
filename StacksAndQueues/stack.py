class Stack:
    """
    A data structure in which the first element in a series of
    elements is accessed last, and the last element in that series is
    accessed first.

    Time complexity of searching: O(n).
    Time complexity of inserting/removing: O(1).

    Last in, first out (LIFO). The last element to be inserted
    is the first one out. Keep a pointer to where the top of the stack
    currently is. Increase the pointer when an object is inserted (pushed)
    into the stack, and decrease it when an object is released (popped)
    from the stack.


    You can also use a linked list to represent a stack, where the top of 
    the stack is represented by the head of the LL.


    Example: 
    Given [1, 2, 3, 4, 5]. Push each item into the stack (starting at index 0 and
    ending at index 4). Then pop each item.

    Currently the stack is []. 
    Pushing 1 onto the stack, you now have [1].
    Pushing 2 onto the stack, you now have [1, 2].
    Pushing 3 onto the stack, you now have [1, 2, 3].
    Pushing 4 onto the stack, you now have [1, 2, 3, 4].
    Pushing 5 onto the stack, you now have [1, 2, 3, 4, 5].

    Popping from the stack, you have processed 5. Now you have [1, 2, 3, 4].
    Popping from the stack, you have processed 4. Now you have [1, 2, 3].
    Popping from the stack, you have processed 3. Now you have [1, 2].
    Popping from the stack, you have processed 2. Now you have [1].
    Popping from the stack, you have processed 1. Now you have [].
    """

    def __init__(self, size=10, first_item=None):
        self.top = 0 # represents the first empty slot in the list
        self.size = abs(size) # do not allow negative sizes
        self.s = [None] * self.size
        if first_item is not None:
            self.s.push(first_item)


    def push(self, item):
        """
        Idea:
        s[top] represents the first empty slot (even if there is something
        there in the list), so put the item at s[top]. Then increment top.
        """
        if self.is_full():
            raise Exception("Stack is full.")
        
        self.s[self.top] = item
        self.top += 1


    def pop(self):
        """
        Idea:
        s[top] represents the first empty slot (even if there is something
        there in the list), so s[top - 1] represents the last item pushed onto the
        stack. Return s[top - 1] and decrement top.
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        self.top -= 1
        return self.s[self.top]


    def peek(self):
        """
        Similar to popping, but the element is not released from the stack. 
        Consequently, top is not updated. 
        """
        if self.is_empty():
            return None
        return self.s[self.top - 1]


    def is_empty(self):
        """ 
        Checks to see if there is nothing in the stack. Top represents the
        first available empty slot. Therefore if top is zero, then the first
        slot in the stack is empty. Consequently the stack is empty.
        """
        return self.top <= 0 


    def is_full(self):
        """
        Checks to see if the stack is full. Top represents the first 
        available empty slot. Therefore if top reaches an index that is out of bounds, 
        then the next available slot is out of bounds. Consequently the stack is 
        full.
        """
        return self.top >= self.size


    def clear(self, *, confirm=False):
        """ 
        Destroys the stack.
        """
        if confirm:
            self.s = [None] * self.size
            self.top = 0



def main():
    string = "abcdefg"
    print("Before: " + string)
    s = Stack()
    for i in range(len(string)):
        s.push(string[i])
    
    result = ""
    while not s.is_empty():
        result = result + s.pop()

    print("After: " + result)

    string = "0123456789"
    print("\nBefore: " + string)

    for c in string:
        s.push(c)
    
    result = ""
    while s.peek() is not None:
        result += s.pop()
    
    print("After: " + result)
    s.clear(confirm=True)
    print("After clearing:", s.s)


    print("\nThis will cause an exception:")
    s = Stack(1)
    s.push(1)
    s.push(2)

if __name__ == "__main__":
    main()