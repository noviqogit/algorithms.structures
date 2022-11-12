# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

from queue import LifoQueue
import unittest


class Solution(LifoQueue):
    def __init__(self):
        super().__init__()
        self.min = LifoQueue()
        self.min.put(float('inf'))

    def peek(self):
        return self.min.queue[-1]

    def push(self, value):
        self.put(value)
        if value <= self.peek():
            self.min.put(value)

    def pop(self):
        value = self._get()
        if self.peek() == value:
            self.min.get()
        return value


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()

    def test_one(self):
        values = [1, 1, 3, 4, 5]
        for value in values[::-1]:
            self.data.push(value)
        self.assertEqual(self.data.peek(), 1)

    def test_two(self):
        values = [1, 1, 3, 4, 5]
        for value in values[::-1]:
            self.data.push(value)
        self.data.pop()
        self.assertEqual(self.data.peek(), 1)

    def test_three(self):
        values = [1, 3, 4, 5]
        for value in values[::-1]:
            self.data.push(value)
        self.data.pop()
        self.assertEqual(self.data.peek(), 3)


if __name__ == "__main__":
    unittest.main()
