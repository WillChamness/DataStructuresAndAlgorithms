class LinkedList:
    class Node:
        def __init__(self, key, value, next):
            # store key along with value to check if key exists when adding/removing
            self.key = key
            self.value = value
            self.next = next


    def __init__(self):
        self.head = None

    
    def add(self, key, value):
        if self.head is None:
            self.head = self.Node(key, value, None)
        else:
            self.head = self.Node(key, value, self.head)
    

    def find(self, key):
        return self._find(key, 0, self.head)

    
    def _find(self, key, i, node):
        if node is None:
            return -1
        elif node.key == key:
            return i
        else:
            return self._find(key, i+1, node.next)

    def remove(self, key):
        if self.head is None:
            return None
        elif self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        
        i = self.find(key)
        if i < 0:
            return None

        node = self.head
        j = 0
        while j != i - 1:
            j = j + 1
            node = node.next   

        value = node.next.value
        node.next = node.next.next
        return value

    def to_list(self):
        result = []
        node = self.head

        while node is not None:
            result.append((node.key, node.value))
            node = node.next
        
        return result


    def get(self, key):
        return self._get(key, self.head)

    def _get(self, key, node):
        if node is None:
            return None
        elif node.key == key:
            return node.value
        else:
            return self._get(key, node.next)