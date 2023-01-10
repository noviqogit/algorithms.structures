# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value
# (which might be positive or negative). Design an algorithm to count the number of paths that
# sum to a given value. The path does not need to start or end at the root or a leaf, but it must
# go downwards (traveling only from parent nodes to child nodes).

import unittest
from implementation import BinaryTree


class Solution(BinaryTree):

    def func(self, target):
        count = 0
        roots = set()
        self.find_roots(self.head, roots)
        for root in roots:
            if root.value == target and root.left and root.right:
                count += 1
            count += self.recr(root, target, 0)
        return count

    def find_roots(self, head, roots):
        if not head:
            return
        roots.add(head)
        self.find_roots(head.left, roots)
        self.find_roots(head.right, roots)

    def recr(self, root, target, sm):
        if not root:
            return 0
        sm += root.value
        if not root.left and not root.right:
            return 1 if sm == target else 0
        return self.recr(root.left, target, sm) + self.recr(root.right, target, sm)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Solution()
        tree = [1, 2, -3, '#', '#', 4, -6, '#', '#', -1, '#', '#', 5, -1, '#', '#', 7, -8, '#', '#', '#']
        self.tree.create_preorder(tree)

    def test_one(self):
        target = 5
        count = self.tree.func(target)
        self.assertEqual(4, count)

    def test_two(self):
        target = -1
        count = self.tree.func(target)
        self.assertEqual(4, count)
