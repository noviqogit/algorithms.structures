import unittest


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def view(self):
        return self.view_recr(self.head)

    def view_recr(self, node):
        if not node:
            return []
        return self.view_recr(node.left) + [node.value] + self.view_recr(node.right)

    def create_preorder(self, preorder: list):
        sequence = iter(preorder)
        self.head = self.create_recr(sequence)
        return self.head

    def create_recr(self, seq):
        val = next(seq)
        if val == '#':
            return
        node = Node(val)
        node.left = self.create_recr(seq)
        node.right = self.create_recr(seq)
        return node


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree()

    def test_one(self):
        arr = [3, 2, 1, '#', '#', '#', 5, 4, '#', '#', 6, '#', '#']
        self.tree.create_preorder(arr)
        self.assertEqual([3, 2, 1, 5, 4, 6], self.tree.view())

    def test_two(self):
        arr = [3, '#', '#']
        self.tree.create_preorder(arr)
        self.assertEqual([3], self.tree.view())
