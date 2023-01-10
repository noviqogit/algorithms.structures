# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value
# (which might be positive or negative). Design an algorithm to count the number of paths that
# sum to a given value. The path does not need to start or end at the root or a leaf, but it must
# go downwards (traveling only from parent nodes to child nodes).

import unittest
from implementation import BinaryTree


class Solution(BinaryTree):

    def func(self, target):
        root = self.head
        arr, sm = [], 0
        self.recr(root, sm, arr)
        return arr.count(target)

    def recr(self, root, sm, arr):
        if not root:
            return
        sm += root.value
        arr.append(sm)
        self.recr(root.left, sm, arr)
        self.recr(root.right, sm, arr)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Solution()
        tree = [1, 2, -3, '#', '#', 4, -6, '#', '#', -1, '#', '#', 5, -1, '#', '#', 7, -8, '#', '#', '#']
        self.tree.create_preorder(tree)

    def test_one(self):
        target = 5
        count = self.tree.func(target)
        self.assertEqual(2, count)
