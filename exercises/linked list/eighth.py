# Loop Detection: Given a circular linked list, implement an algorithm that returns
# the node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to
# an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [thesameCasearlier] Output: C
import unittest
from implementation import SingleLinkedList


def is_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    else:
        return None
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return slow.value


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = SingleLinkedList()
        self.func = is_cycle

    def test_one(self):
        tail = [3, 4]
        head = [1, 2]
        for value in tail:
            self.data.addAtTail(value)
        node = runner = self.data.head
        for value in head:
            self.data.addAtHead(value)
        while runner.next:
            runner = runner.next
        runner.next = node
        self.assertEqual(self.func(self.data.head), 3)

    def test_two(self):
        tail = [2]
        head = [1]
        for value in tail:
            self.data.addAtTail(value)
        runner = self.data.head
        for value in head:
            self.data.addAtHead(value)
        runner.next = self.data.head
        self.assertEqual(self.func(self.data.head), 1)

    def test_three(self):
        tail = [1]
        head = []
        for value in tail:
            self.data.addAtTail(value)
        self.assertEqual(self.func(self.data.head), None)


if __name__ == "__main__":
    unittest.main()
