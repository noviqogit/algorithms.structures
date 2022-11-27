# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differ by more than one.

import unittest
from exer2 import BalancedBinarySearchTree
from implementation import Node


def func(node, heigh=0):
    if not node:
        return heigh
    left = func(node.left, heigh + 1)
    right = func(node.right, heigh + 1)
    if abs(left - right) > 1:
        return 0
    return max(left, right)


def change_balance(node):
    while node.right:
        node = node.right
    for _ in range(3):
        node.right = Node(node.value + 1)
        node = node.right


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        self.assertTrue(func(self.tree.head))

    def test_two(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        change_balance(self.tree.head)
        self.assertFalse(func(self.tree.head))
