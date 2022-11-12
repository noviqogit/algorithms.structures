# Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

from queue import LifoQueue
import unittest


class Solution:
    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, value):
        self.s1.put(value)

    def sort(self):
        while self.s1.queue:
            num1 = self.s1.get()
            while self.s2.queue:
                num2 = self.s2.get()
                if num1 <= num2:
                    self.s2.put(num2)
                    self.s2.put(num1)
                    break
                else:
                    self.s1.put(num2)
            else:
                self.s2.put(num1)
        self.s1, self.s2 = self.s2, self.s1
        return self.s1.queue


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()

    def test_one(self):
        for val in [3, 5, 1, 7, 2]:
            self.data.push(val)
        self.data.sort()
        self.assertEqual(self.data.s1.queue, [7, 5, 3, 2, 1])

    def test_two(self):
        for val in [1, 2]:
            self.data.push(val)
        self.data.sort()
        self.assertEqual(self.data.s1.queue, [2, 1])

    def test_three(self):
        for val in [9, 2, 2, 3, 3, 9]:
            self.data.push(val)
        self.data.sort()
        self.assertEqual(self.data.s1.queue, [9, 9, 3, 3, 2, 2])


if __name__ == "__main__":
    unittest.main()
