# Successor: Write an algorithm to find the "next" node (i.e., in-order successor)
# of a given node in a binary search tree. You may assume that each node has a link to its parent.

import unittest
from exer2 import BalancedBinarySearchTree


def func(node, value, prev=None):
    if not node:
        return
    if node.value == value:
        return prev.value if prev else None
    if node.value < value:
        return func(node.right, value, node)
    if node.value >= value:
        return func(node.left, value, node)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.create_from_arr(arr)
        successor = func(self.tree.head, 2)
        self.assertEqual(3, successor)

    def test_two(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.create_from_arr(arr)
        successor = func(self.tree.head, 3)
        self.assertEqual(None, successor)

    def test_three(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.tree.create_from_arr(arr)
        successor = func(self.tree.head, 5)
        self.assertEqual(6, successor)
