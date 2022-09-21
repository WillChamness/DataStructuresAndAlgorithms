
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.value_count = 0
        self.table = []
        for i in range(size):
            self.table.append(LinkedList())

    def hash(self, key):
        result = 0
        s = str(key)
        for c in s:
            result = result + ord(c)
        result = result % self.size

        return result
    
    def add(self, key, value):
        index = self.hash(key)
        
        if self.table[index].find(key) < 0: # key/value not found. Add key/value
            self.table[index].add(key, value)
            self.value_count = self.value_count + 1
            self.rehash()
    
    def remove(self, key):
        index = self.hash(key)
        if self.table[index].find(key) >= 0: # key/value found. Extract value
            self.value_count = self.value_count - 1
            return self.table[index].remove(key)