# Palindrome: Implement a function to check if a LinkedList is a palindrome.
from implementation import SingleLinkedList
from queue import LifoQueue
import unittest


class Solution(SingleLinkedList):
    def is_palindrome(self):
        slow = fast = self.head
        if not slow:
            return False
        elif not slow.next:
            return True
        stack = LifoQueue()
        while fast and fast.next:
            stack.put(slow)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        while slow:
            node = stack.get()
            if node.value != slow.value:
                return False
            slow = slow.next
        return True


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()
        self.func = self.data.is_palindrome

    def test_one(self):
        nodes = []
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), False)

    def test_two(self):
        nodes = [1]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), True)

    def test_three(self):
        nodes = [1, 3, 1]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), True)

    def test_four(self):
        nodes = [1, 2, 2, 1]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), True)

    def test_five(self):
        nodes = [1, 2, 3, 1]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), False)


if __name__ == "__main__":
    unittest.main()
