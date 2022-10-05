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
        for item in self.array:
            print(item)

    def __len__(self):
        return self.size

arr = Array(5)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.traverse()
