# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.


import unittest
from implementation import BinaryTree, Node


class BalancedBinarySearchTree(BinaryTree):

    def create(self, arr):
        n = len(arr)
        if not n:
            return
        if n == 1:
            node = Node(arr[0])
            return node
        middle = n // 2
        node = Node(arr[middle])
        node.left = self.create(arr[:middle])
        node.right = self.create(arr[middle + 1:])
        return node


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        self.assertEqual([1, 2, 3, 4, 5], self.tree.view())

    def test_two(self):
        arr = [2, 3, 4, 5]
        self.tree.head = self.tree.create(arr)
        self.assertEqual([2, 3, 4, 5], self.tree.view())
