# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.
# EXAMPLE
# lnput:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

from implementation import SingleLinkedList
import unittest


class Solution(SingleLinkedList):
    def find_middle(self):
        if not (self.head and self.head.next):
            return []
        slow = self.head
        fast = self.head.next.next
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        result = self.view()
        return result


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()
        self.func = self.data.find_middle

    def test_one(self):
        nodes = [1]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), [])

    def test_two(self):
        nodes = [1, 2, 3, 4, 5]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), [1, 2, 4, 5])

    def test_three(self):
        nodes = [1, 2, 3, 4]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), [1, 3, 4])

    def test_four(self):
        nodes = []
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), [])

    def test_five(self):
        nodes = [1, 2]
        for node in nodes:
            self.data.addAtTail(node)
        self.assertEqual(self.func(), [1])


if __name__ == "__main__":
    unittest.main()
