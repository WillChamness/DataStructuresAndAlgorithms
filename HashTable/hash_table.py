from linked_list import LinkedList

class HashTable:
    """ 
    A.K.A. dictionaries in Python.

    Simple implementation of a hash table. Uses chaining to deal with collisions.
    
    Strategy: 
    Take a string and convert it to a number. Use this number to represent the index of
    a list. Add/remove/modify a value at that index. 

    You can also use linear or quadratic probing to deal with collisions.

    See the hash function for an example and "Hash table with chaining.png" for an illustration.
    """
    OPTIMAL_LAMDA = 1

    def __init__(self, size=10):
        self.size = size # i.e. m
        self.item_count = 0 # i.e. n
        self.table = []
        for i in range(size):
            self.table.append(LinkedList())

    def hash(self, key):
        """ 
        Simple hashing function. Takes a string and returns the total unicode value of each character
        mod the table size. Note that this implementation is far from optimal.
        """
        result = 0
        s = str(key)
        for c in s:
            result = result + ord(c)
        result %= self.size

        return result
    
    def add(self, key, value):
        """ 
        Adds the key/value pair of to the table using the above hashing function.
        Note that table[i] represents a linked list.
        """
        index = self.hash(key)
        
        if self.table[index].find(key) < 0: # key/value not found. Add key/value
            self.table[index].add(key, value)
            self.item_count += 1
            self.rehash()
    
    def remove(self, key):
        """ 
        Removes the key/value pair of the table using the above hashing function. 
        Note that table[i] represents a linked list.
        """
        index = self.hash(key)
        if self.table[index].find(key) >= 0: # key/value found. Extract value
            self.item_count -= 1
            return self.table[index].remove(key)

    def get_value(self, key):
        """ 
        Returns the value with the associated key using the above hashing function.
        """
        index = self.hash(key)
        return self.table[index].get(key)
    
    def modify(self, key, new_value):
        """ 
        Given a key, set the assocuated value to something new.
        """
        index = self.hash(key)
        results = self.table[index].remove(key)
        if results is not None: # key/value found. Create new key/value pair
            self.table[index].add(key, new_value)
    
    def lamda(self):
        """ 
        Returns lamda, the ratio of the number of items to the table size.
        The optimal lamda for this implementation is 1.
        """
        return self.item_count / self.size

    def rehash(self):
        """ 
        Copies the data to a new table. The new size is twice the previous. Must perform 
        above hashing function with new table size.
        """ 
        if self.lamda() <= HashTable.OPTIMAL_LAMDA:
            return
        
        old_table = self.table
        self.size *= 2
        self.table = []
        
        for i in range(self.size):
            self.table.append(LinkedList())

        for i in range(len(old_table)):
            backup = old_table[i].to_list()
            for j in range(len(backup)):
                self.add(backup[j][0], backup[j][1])
                self.item_count -= 1 # not actually adding a new key/value pair