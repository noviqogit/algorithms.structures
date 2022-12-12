# Validate BST: Implement a function to check if a binary tree is a binary search tree.

import unittest
from implementation import BinaryTree


def is_binary_search(node):
    left = node.left.value if node.left else node.value
    right = node.right.value if node.right else node.value + 1
    return left <= node.value < right


def func(node, minimum=None, maximum=None):
    if not node:
        return True
    if minimum and node.value < minimum:
        return False
    if maximum and node.value > maximum:
        return False
    if is_binary_search(node):
        return func(node.left, minimum, node.value) and func(node.right, node.value, maximum)
    return False


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree()

    def test_one(self):
        arr = [3, 2, 1, '#', '#', '#', 5, 4, '#', '#', 6, '#', '#']
        head = self.tree.create_preorder(arr)
        self.assertTrue(func(head))

    def test_two(self):
        arr = [3, 2, 1, '#', '#', 4, '#', '#', 5, 4, '#', '#', 6, '#', '#']
        head = self.tree.create_preorder(arr)
        self.assertFalse(func(head))
