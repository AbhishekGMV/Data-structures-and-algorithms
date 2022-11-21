class Array:
    """"
    Implementation of static arrays
    """

    def __init__(self, size) -> None:
        self.size = size
        self.array = []

    def append(self, item):
        if self.size == 0:
            raise Exception("Array index out of bounds")
        self.array.append(item)
        self.size -= 1

    def traverse(self):
        for item in self.array:
            print(item)

    def find(self, value):
        for index in range(len(self.array)):
            if self.array[index] == value:
                return index
        return -1

    def isEmpty(self):
        return len(self.array) == 0

    def __len__(self):
        return self.size


arr = Array(5)
print(arr.isEmpty())
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
print("Found at index: ", arr.find(2))
print("Found at index: ", arr.find(20))
arr.append(5)
arr.traverse()
print(arr.isEmpty())
