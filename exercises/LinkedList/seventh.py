# Intersection: Given two (singly) linked lists, determine if the two lists intersect.
# Return the intersecting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first LinkedList is the exact same node (by reference) as the jth node
# of the second LinkedList, then they are intersecting.
import unittest
from implementation import SingleLinkedList


def get_intersection_node(headA, headB):
    i = j = 0
    node = headA
    while node:
        i += 1
        node = node.next
    node = headB
    while node:
        j += 1
        node = node.next
    if i < j:
        node, another = headB, headA
    else:
        another, node = headB, headA
    step = abs(i - j)
    for _ in range(step):
        node = node.next
    while node and another:
        if node == another:
            return node.value
        node, another = node.next, another.next
    return False


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.first = SingleLinkedList()
        self.second = SingleLinkedList()
        self.func = get_intersection_node

    def test_one(self):
        A = [[], [1, 2]]
        B = [3, 4]
        for value in A[1]:
            self.first.addAtTail(value)
        self.second.head = self.first.head
        for value in A[0]:
            self.first.addAtHead(value)
        for value in B:
            self.second.addAtHead(value)
        self.assertEqual(self.func(self.first.head, self.second.head), 1)

    def test_two(self):
        A = [[1, 2], [5, 6]]
        B = [3, 4]
        for value in A[1]:
            self.first.addAtTail(value)
        self.second.head = self.first.head
        for value in A[0]:
            self.first.addAtHead(value)
        for value in B:
            self.second.addAtHead(value)
        self.assertEqual(self.func(self.first.head, self.second.head), 5)

    def test_three(self):
        A = [[1, 2], [4, 5]]
        B = [3]
        for value in A[1]:
            self.first.addAtTail(value)
        self.second.head = self.first.head
        for value in A[0]:
            self.first.addAtHead(value)
        for value in B:
            self.second.addAtHead(value)
        self.assertEqual(self.func(self.first.head, self.second.head), 4)

    def test_four(self):
        A = [[], [1, 2]]
        B = [3, 4]
        for value in A[1]:
            self.first.addAtTail(value)
        for value in A[0]:
            self.first.addAtHead(value)
        for value in B:
            self.second.addAtHead(value)
        self.assertEqual(self.func(self.first.head, self.second.head), False)


if __name__ == "__main__":
    unittest.main()
