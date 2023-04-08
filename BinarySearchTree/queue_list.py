class QueueList:
    def __init__(self, size=10, first_item=None):
        self.head = 0 
        self.tail = 0 
        self.counter = 0 
        self.size = size
        self.q = []


    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        
        if len(self.q) <= self.tail:
            self.q.append(item)
        else: 
            self.q[self.tail] = item
        
        self.counter = self.counter + 1
        self.tail = (self.tail + 1) % self.size


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
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
