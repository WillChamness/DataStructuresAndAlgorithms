class ArrayList:
    def __init__(self, initial_size=10, initial_item=None):
        self.size = initial_size
        self.array = [None] * initial_size
        self.pointer = 0

        if initial_item is not None:
            self.add(initial_item)
