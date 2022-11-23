# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differ by more than one.

import unittest
from exer2 import create_tree


def func(node, heigh):
    if not node:
        return heigh
    left = func(node.left, heigh)
    right = func(node.right, heigh)
    if abs(left - right) > 1:
        return 0
    return max(left, right)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.view = []

    def test_one(self):
        tree = create_tree([1, 2, 3, 4, 5], self.view)
        self.assertEqual(bool(func(tree, 1)), True)

    def test_two(self):
        tree = create_tree([1, 2, 3, 4, 5, 6, 7, 8, 9], self.view, unbalanced=True)
        print(self.view)
        self.assertEqual(bool(func(tree, 0)), False)
