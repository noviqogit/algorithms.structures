# Validate BST: Implement a function to check if a binary tree is a binary search tree.

import unittest
from exer2 import BalancedBinarySearchTree, Node


def is_binary_search(node):
    left = node.left.value if node.left else node.value
    right = node.right.value if node.right else node.value + 1
    return left <= node.value < right


def func(node):
    if not node:
        return True
    if is_binary_search(node):
        return func(node.left) and func(node.right)
    return False


def set_not_binary(node):
    while node.right:
        node = node.right
    node.left = Node(node.value + 1)


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
        set_not_binary(self.tree.head)
        self.assertFalse(func(self.tree.head))
