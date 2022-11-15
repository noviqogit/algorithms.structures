# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.


import unittest


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def create_tree(arr, view):
    n = len(arr)
    if not n:
        return
    if n == 1:
        node = Node(arr[0])
        view.append(node.value)
        return node
    middle = n // 2
    node = Node(arr[middle])
    view.append(node.value)
    node.left = create_tree(arr[:middle], view)
    node.right = create_tree(arr[middle + 1:], view)
    return node


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.func = create_tree
        self.view = []

    def test_one(self):
        self.func([1, 2, 3, 4, 5], self.view)
        self.assertEqual(self.view, [3, 2, 1, 5, 4])

    def test_two(self):
        self.func([1, 2, 3, 4], self.view)
        self.assertEqual(self.view, [3, 2, 1, 4])
