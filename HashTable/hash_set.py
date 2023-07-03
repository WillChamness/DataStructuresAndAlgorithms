from hash_table import HashTable

class HashSet(HashTable):
    def __init__(self):
        super().__init__()
    

    def add(self, item):
        if not self.contains(item):
            super().add(item, item)
    

    def remove(self, item):
        if self.contains(item):
            super().remove(item)
    

    def contains(self, item):
        return self.table[self.hash(item)].find(item) >= 0

    

def main():
    hs = HashSet()
    hs.add(1)
    hs.add(2)
    hs.add(3)
    print("HashSet contains 1:", hs.contains(1))
    print("HashSet contains -1:", hs.contains(-1))
    hs.remove(1)
    print("HashSet contains 1 after removing:", hs.contains(1))
    hs.add(2)
    print("HashSet after adding 2 again:")
    lst = []
    for i in range(len(hs.table)):
        lst.append(hs.table[i].to_list())
    print(lst)

    print("HashSet after containing multiple unique keys with the same hash:")
    hs = HashSet()
    hs.add("e")
    hs.add("ed")
    hs.add("edd")
    hs.add("eddd")
    hs.add("edddd")
    lst = []
    for i in range(len(hs.table)):
        lst.append(hs.table[i].to_list())
    print(lst)


if __name__ == "__main__":
    main()