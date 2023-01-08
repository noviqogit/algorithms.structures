# Random Node: You are implementing a binary search tree class from scratch, which, in addition to insert,
# find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should
# be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you
# would implement the rest of the methods

from exer2 import BalancedBinarySearchTree, Node
import unittest
from random import choice


class Solution(BalancedBinarySearchTree):

    def set_tree(self, arr):
        self.arr = arr
        self.head = super().create_from_arr(arr)
        return self.head

    def find(self, root, val):
        if not root:
            return None
        if root.value == val:
            return root
        if root.value < val:
            return self.find(root.right, val)
        return self.find(root.left, val)

    def insert_recr(self, root, val):
        if not root:
            return Node(val)
        if root.value < val:
            root.right = self.insert_recr(root.right, val)
        else:
            root.left = self.insert_recr(root.left, val)
        return root

    def insert(self, root, val):
        self.arr.append(val)
        return self.insert_recr(root, val)

    def delete(self, root, key):
        self.arr.remove(key)
        self.delete_recr(root, key)

    def delete_recr(self, root, key):
        if not root:
            return None
        if root.value == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = root.right
            while node.left:
                node = node.left
            root.val = node.val
            root.right = self.delete_recr(root.right, node.val)
        if key > root.value:
            root.right = self.delete_recr(root.right, key)
        if key < root.value:
            root.left = self.delete_recr(root.left, key)
        return root

    def getRandomNone(self):
        return choice(self.arr())


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Solution()
        arr = [1, 2, 5, 7, 12]
        self.root = self.tree.set_tree(arr)

    def test_one(self):
        self.assertTrue(self.tree.find(self.root, 1))

    def test_two(self):
        self.assertFalse(self.tree.find(self.root, 6))

    def test_three(self):
        self.tree.insert(self.root, 6)
        self.assertEqual([1, 2, 5, 7, 12, 6], self.tree.arr)

    def test_four(self):
        self.tree.delete(self.root, 2)
        self.assertEqual([1, 5, 7, 12], self.tree.arr)
