class Array:
    """"
    Implementation of static arrays
    """
    array = []

    def __init__(self, size) -> None:
        self.size = size

    def append(self, item):
        """
        Add to end to array
        """
        if self.size == 0:
            raise Exception("Array index out of bounds")
        self.array.append(item)
        self.size -= 1

    def traverse(self):
        """
        Read array items
        """
        if self.size == 0:
            return

        for item in self.array:
            print(item)

    def find(self, value):
        for index in range(len(self.array)):
            if self.array[index] == value:
                return index
        return -1

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size


arr = Array(5)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.traverse()
