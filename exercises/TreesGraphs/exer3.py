# List of Depths: Given a binary tree, design an algorithm which creates
# a linked list of all the nodes at each depth (e.g., if you have a tree
# with depth D, you'll have D linked lists).

import unittest
from exercises.LinkedList.implementation import SingleLinkedList
from exer2 import BalancedBinarySearchTree


def func(node, _list: SingleLinkedList):
    if not node:
        return
    func(node.left, _list)
    _list.addAtTail(node.value)
    func(node.right, _list)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.list = SingleLinkedList()
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        func(self.tree.head, self.list)
        self.assertEqual(self.list.view(), [1, 2, 3, 4, 5])

    def test_two(self):
        arr = [2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        func(self.tree.head, self.list)
        self.assertEqual(self.list.view(), [2, 3, 4, 5])
