class Stack:
    def __init__(self, size=10, first_item=None):
        self.s = []
        for i in range(size):
            self.s.append(None)
        self.top = 0
        self.size = abs(size)
        if first_item is not None:
            self.s.push(first_item)

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full.")
        
        self.s[self.top] = item
        self.top = self.top + 1

    def pop(self):
        if self.is_empty():
            return None

        self.top = self.top - 1
        return self.s[self.top]

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top >= self.size


def main():
    string = "abcdefg"
    print("Before: " + string)
    s = Stack(len(string))
    for i in range(len(string)):
        s.push(string[i])
    
    result = ""
    while not s.is_empty():
        result = result + s.pop()

    print("After: " + result)

if __name__ == "__main__":
    main()