# Successor: Write an algorithm to find the "next" node (i.e., in-order successor)
# of a given node in a binary search tree. You may assume that each node has a link to its parent.

import unittest
from exer2 import BalancedBinarySearchTree


def func(node, value):
    parent = None
    while node.value != value:
        if node.value > value:
            parent = node
            node = node.left
        elif node.value < value:
            parent = node
            node = node.right
    if not node.right:
        if parent is None:
            return None
        return parent.value if node.value < parent.value else None
    node = node.right
    while node.left:
        node = node.left
    return node.value


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        _next = func(self.tree.head, 2)
        self.assertEqual(3, _next)

    def test_two(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        _next = func(self.tree.head, 5)
        self.assertEqual(None, _next)

    def test_three(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.tree.head = self.tree.create(arr)
        _next = func(self.tree.head, 5)
        self.assertEqual(6, _next)
