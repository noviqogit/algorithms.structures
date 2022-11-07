# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from implementation import SingleLinkedList
import unittest


class Solution(SingleLinkedList):
    def run(self, k):
        if k > self.size:
            return
        node = runner = self.head
        for _ in range(k):
            runner = runner.next
        while runner.next:
            runner, node = runner.next, node.next
        return node.value


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()
        self.func = self.data.run

    def test_one(self):
        nodes = [1, 2, 3, 4, 5]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(0), 5)

    def test_two(self):
        nodes = [1, 2, 3, 4, 5]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(1), 4)

    def test_three(self):
        nodes = [1, 2, 3, 4, 5]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(2), 3)

    def test_four(self):
        nodes = [1]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(6), None)


if __name__ == "__main__":
    unittest.main()
