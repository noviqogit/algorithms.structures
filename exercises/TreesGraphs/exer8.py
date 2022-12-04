# First Common Ancestor: Design an algorithm and write code to find the first common
# ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

import unittest
from exer2 import BalancedBinarySearchTree, Node


def common_ancestor(tree, one, two):
    first = find_path(tree, one, ())
    second = find_path(tree, two, ())
    lenght = min(len(first), len(second)) - 1
    first, second = first[:lenght], second[:lenght]
    for node, _node in zip(first[::-1], second[::-1]):
        if node == _node:
            return node


def find_path(tree, target, path):
    if not tree:
        return
    path += (tree.value,)
    if tree == target:
        return path
    left = find_path(tree.left, target, path)
    right = find_path(tree.right, target, path)
    return left if left else right


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        node = self.tree.head
        while node.right:
            node = node.right
        one = node.right = Node(node.value)
        while node.left:
            node = node.left
        two = node.left = Node(self.tree.head.value)
        self.assertEqual(5, common_ancestor(self.tree.head, one, two))

    def test_two(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        node = self.tree.head
        while node.left:
            node = node.left
        one = node.right = Node(self.tree.head.value)
        node = self.tree.head
        while node.right:
            node = node.right
        two = node
        self.assertEqual(3, common_ancestor(self.tree.head, one, two))
