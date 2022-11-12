# Three in One: Describe how you could use a single array to implement three stacks.


class Stack:
    def __init__(self, array: list, head: int):
        self.array = array
        self.array[head] = 0
        self.head = head

    def is_empty(self):
        return False if self.array[self.head] else True

    def peek(self):
        if not self.is_empty():
            index = self.head + self.array[self.head] * 3
            return self.array[index]

    def put(self, value):
        index = self.head + 3 + self.array[self.head] * 3
        if index < len(self.array):
            self.array[index] = value
            self.array[self.head] += 1

    def get(self):
        if not self.is_empty():
            index = self.head + self.array[self.head] * 3
            result = self.array[index]
            self.array[index] = None
            self.array[self.head] -= 1
            return result


arr = [None for _ in range(9)]
stacks = [Stack(arr, i) for i in range(3)]
