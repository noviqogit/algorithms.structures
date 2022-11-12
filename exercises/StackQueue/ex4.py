# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
from queue import LifoQueue
import unittest


class Solution:
    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, value):
        self.s1.put(value)

    def pop(self):
        if not self.s2.queue:
            while self.s1.queue:
                self.s2.put(self.s1.get())
        return self.s2.get()


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()
        for val in [1, 2, 3, 4, 5]:
            self.data.push(val)

    def test_one(self):
        self.assertEqual(self.data.pop(), 1)

    def test_two(self):
        self.data.pop()
        for val in [6, 7, 8, 9, 10]:
            self.data.push(val)
        self.assertEqual(self.data.pop(), 2)


if __name__ == "__main__":
    unittest.main()
