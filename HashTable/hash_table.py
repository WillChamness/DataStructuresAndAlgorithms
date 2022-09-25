
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
        """ 
        Adds the key/value pair of to the table using the above hashing function.
        Note that table[i] represents a linked list, so table[i].add() is a function
        of the linked list. 
        """
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

    def get_value(self, key):
        index = self.hash(key)
        return self.table[index].get(key)