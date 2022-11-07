# Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list the values of x only need to be after the
# elements less than x (see below). The partition element x can appear anywhere
# in the "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
# Output:  3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from implementation import SingleLinkedList, Node
import unittest


def partition(main, target):
    node = main.head
    if not node:
        return []
    elif not node.next:
        return node
    head = less = Node()
    tail = more = Node()
    while node:
        if node.value < target:
            less.next = Node(node.value)
            less = less.next
        else:
            more.next = Node(node.value)
            more = more.next
        node = node.next
    less.next = tail.next
    return head.next


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = SingleLinkedList()
        self.func = partition

    def test_one(self):
        nodes = []
        for node in nodes:
            self.data.addAtTail(node)
        self.data.head = self.func(self.data, 1)
        self.assertEqual(self.data.view(), [])

    def test_two(self):
        nodes = [1]
        for node in nodes:
            self.data.addAtTail(node)
        self.data.head = self.func(self.data, 1)
        self.assertEqual(self.data.view(), [1])

    def test_three(self):
        nodes = [3, 5, 8, 5, 10, 2, 1]
        for node in nodes:
            self.data.addAtTail(node)
        self.data.head = self.func(self.data, 5)
        self.assertEqual(self.data.view(), [3, 2, 1, 5, 8, 5, 10])


if __name__ == "__main__":
    unittest.main()
