# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high,
# it might topple. Therefore, in real life, we would likely start a new stack when
# the previous stack exceeds some threshold. Implement a data structure SetOfStacks
# that mimics this. SetOfStacks should be composed of several stacks and should create
# a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
# should behave identically to a single stack (that is, pop() should return the same values as
# it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub stack.

from queue import LifoQueue
import unittest


class Solution(LifoQueue):

    def __init__(self, size):
        super().__init__()
        self.size = size

    def push(self, value):
        if not self.queue:
            new = LifoQueue(self.size)
            new.put(value)
            self.put(new)
        else:
            stack = self.get()
            if stack.qsize() < self.size:
                stack.put(value)
                self.put(stack)
            else:
                new = LifoQueue(self.size)
                new.put(value)
                self.put(stack)
                self.put(new)

    def popAT(self, index=1):
        if self.qsize() >= index:
            return self.queue.pop(-index)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution(3)

    def test_one(self):
        values = [1, 2, 3, 4, 5]
        for value in values[::-1]:
            self.data.push(value)
        self.assertEqual(self.data.qsize(), 2)

    def test_two(self):
        values = [1, 1, 3]
        for value in values[::-1]:
            self.data.push(value)
        self.assertEqual(self.data.qsize(), 1)

    def test_three(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        for value in values[::-1]:
            self.data.push(value)
        self.assertEqual(self.data.qsize(), 3)


if __name__ == "__main__":
    unittest.main()
