class QueueList:
    """ 
    A data structure in which the first element inserted is
    the first element to be accessed. 

    Time complexity of searching: O(n).
    Time complexity of inserting/removing: O(1).

    Strategy: First in, first out (FIFO). The first element in
    is the first element out. Keep a pointer to the next available
    slot, and keep a pointer to the next item to be released. Note
    that tail can be less than head when, for example, tail reaches 
    the end and index 0 is open. Also a counter is needed to tell
    if the queue is full or empty since abs(head - tail) == 0 ==> the
    queue is either full or empty.

    You can also use a doubly linked list to represent a queue, where
    the head of the queue is represented by the head of the LL and the
    tail of the queue is represented by the tail of the LL.

    Note: 
    The class is named QueueList because there is a built in python
    module named queue.


    Example:
    Given [1, 2, 3, 4, 5]. Enqueue each item to the queue (starting at index 0,
    ending at index 4). Then dequeue each item.

    Currently the queue is []. 
    Enqueuing 1, you now have [1].
    Enqueuing 2, you now have [1, 2].
    Enqueuing 3, you now have [1, 2, 3].
    Enqueuing 4, you now have [1, 2, 3, 4].
    Enququing 5, you now have [1, 2, 3, 4, 5].

    Dequeuing, you have processed 1. Now you have [2, 3, 4, 5].
    Dequeuing, you have processed 2. Now you have [3, 4, 5].
    Dequeuing, you have processed 3. Now you have [4, 5].
    Dequeuing, you have processed 4. Now you have [5].
    Dequeuing, you have processed 5. Now you have [].
    """
    def __init__(self, size=10, first_item=None):
        self.head = 0 # points to the next item to be released
        self.tail = 0 # points to the next available empty slot
        self.counter = 0 # represents the total number of items in the queue
        self.size = size
        self.q = []

    def enqueue(self, item):
        """
        Idea:
        q[tail] represents the next available slot (even if there is something
        in the list), so put the item at q[tail]. Then increment tail.
        """
        if self.is_full():
            raise Exception("Queue is full")
        
        if len(self.q) <= self.tail: # must append to list when initially creating queue
            self.q.append(item)
        else: 
            self.q[self.tail] = item
        
        self.counter = self.counter + 1
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        """
        Idea:
        q[head] represents the item at the front of the queue, so get the item
        at q[head], increment q[head], and return the item.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.q[self.head]
        self.head = (self.head + 1) % self.size
        self.counter = self.counter - 1
        return item
    
    def next(self):
        """ 
        Similar to dequeue, but the item is not released from the queue.
        Therefore head is not modified.
        """
        if self.is_empty():
            return None
        return self.q[self.head]

    def is_empty(self):
        """ 
        Returns true when the item count is zero.
        """
        return self.counter == 0
    
    def is_full(self):
        """ 
        Returns true when the item count is
        equal to the queue size.
        """
        return self.counter == self.size



def main():
    q = QueueList()
    before = ""
    for i in range (q.size):
        before += str(i)
    print("Before: " + before)
    for c in before:
        q.enqueue(c)

    after = ""
    while not q.is_empty():
        after += q.dequeue()
    print("After: " + after)

    before = "abcdefg"
    print("\nBefore: " + before)
    for c in before:
        q.enqueue(c)
    
    after = ""
    while q.next() is not None:
        after += q.dequeue()
    
    print("After: " + after)

    before = "xyzabcd"
    print("\nBefore: " + before)
    
    q = QueueList(len(before))
    for c in before:
        q.enqueue(c)
    q.dequeue()
    q.enqueue("e")
    q.dequeue()
    q.enqueue("f")
    q.dequeue()
    q.enqueue("g")

    after = ""
    while not q.is_empty():
        after += q.dequeue()
    
    print("After: " + after)

    print("\nThis will cause an exception:")
    q = QueueList(1)
    q.enqueue(1)
    q.enqueue(2)

if __name__ == "__main__":
    main()