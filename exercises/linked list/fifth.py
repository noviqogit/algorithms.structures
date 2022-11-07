# Sum Lists: You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's digit is at
# the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).
# That is 617 + 295.
# Output: 2 -> 1 -> 9.
# That is 912.
# FOLLOW UP
# Suppose the digits are stored in forward order.
# Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).
# That is 617 + 295.
# Output:9 ->1 -> 2.
# That is 912.

import unittest
from implementation import SingleLinkedList


def revers(one, another):
    number = 0
    for node in (one.head, another.head):
        rank = 1
        while node:
            number += node.value * rank
            rank *= 10
            node = node.next
    data = SingleLinkedList()
    for value in str(number):
        data.addAtHead(int(value))
    return data


def forward(one, another):
    number = 0
    for node in (one.head, another.head):
        rank = 1
        arr = []
        while node:
            arr.append(node.value)
            node = node.next
        for value in arr[::-1]:
            number += value * rank
            rank *= 10
    data = SingleLinkedList()
    for value in str(number)[::-1]:
        data.addAtHead(int(value))
    return data


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.first = SingleLinkedList()
        self.second = SingleLinkedList()
        self.func = forward

    def test_one(self):
        first, second = [7, 1, 6], [5, 9, 2]
        for node in first:
            self.first.addAtTail(node)
        for node in second:
            self.second.addAtTail(node)
        self.data = self.func(self.first, self.second)
        self.assertEqual(self.data.view(), [1, 3, 0, 8])

    def test_two(self):
        first, second = [7, 1, 6], []
        for node in first:
            self.first.addAtTail(node)
        for node in second:
            self.second.addAtTail(node)
        self.data = self.func(self.first, self.second)
        self.assertEqual(self.data.view(), [7, 1, 6])


if __name__ == "__main__":
    unittest.main()
