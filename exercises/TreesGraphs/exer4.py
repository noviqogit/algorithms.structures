# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differ by more than one.

import unittest
from implementation import BinaryTree


def func(node, heigh=0):
    if not node:
        return heigh
    left = func(node.left, heigh + 1)
    right = func(node.right, heigh + 1)
    if abs(left - right) > 1:
        return 0
    return max(left, right)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree()

    def test_one(self):
        arr = [3, 2, 1, '#', '#', '#', 5, 4, '#', '#', 6, 1, '#', '#', '#']
        head = self.tree.create_preorder(arr)
        self.assertTrue(func(head))

    def test_two(self):
        arr = [3, 2, 1, '#', '#', '#', 5, 4, '#', '#', 6, 1, '#', 7, '#', '#', '#']
        head = self.tree.create_preorder(arr)
        self.assertFalse(func(head))
