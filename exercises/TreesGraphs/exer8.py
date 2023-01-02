# First Common Ancestor: Design an algorithm and write code to find the first common
# ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

import unittest
from implementation import BinaryTree


def common_ancestor(tree, one, two):
    if not tree:
        return None
    if tree.value in (one, two):
        return tree
    left = common_ancestor(tree.left, one, two)
    right = common_ancestor(tree.right, one, two)
    if not left and not right:
        return None
    if left and right:
        return tree
    return left if left else right


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree()

    def test_one(self):
        arr = [7, 2, 1, '#', '#', '#', 5, 4, '#', '#', 6, 1, '#', '#', '#']
        head = self.tree.create_preorder(arr)
        node = common_ancestor(head, 4, 6)
        self.assertEqual(5, node.value)

    def test_two(self):
        arr = [7, 2, 1, '#', '#', '#', 5, 4, '#', '#', 6, 1, '#', '#', '#']
        head = self.tree.create_preorder(arr)
        node = common_ancestor(head, 1, 6)
        self.assertEqual(7, node.value)
