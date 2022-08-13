class QueueList:
    def __init__(self, size=10, first_item=None):
        self.head = 0 # points to the next item to be released
        self.tail = 0 # points to the next available empty slot
        self.counter = 0 # represents the total number of items in the queue
        self.size = size
        self.q = []

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        
        if len(self.q) <= self.tail:
            self.q.append(item)
        else: 
            self.q[tail] = item
        
        self.counter = self.counter + 1
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            return None
        
        item = self.q[self.head]
        self.head = (self.head + 1) % self.size
        self.counter = self.counter - 1
        return item
    
    def next(self):
        if self.is_empty():
            return None
        return self.q[self.head]

    def is_empty(self):
        return self.counter == 0
    
    def is_full(self):
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

    q = QueueList(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("\nNext: " + str(q.next()))
    q.dequeue()
    print("Next: " + str(q.next()))

    q = QueueList(1)
    q.enqueue(1)
    print("\n" + str(q.dequeue()))
    print(q.dequeue())

    print("\nThis will cause an exception:")
    q = QueueList(1)
    q.enqueue(1)
    q.enqueue(2)

if __name__ == "__main__":
    main()