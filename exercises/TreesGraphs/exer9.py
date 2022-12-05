# BST Sequences: A binary search tree was created by traversing through an array from
# left to right and inserting each element. Given a binary search tree with distinct elements,
# print all possible arrays that could have led to this tree.

from itertools import permutations
import unittest
from exer2 import BalancedBinarySearchTree


def find_sequences(root):
    if not root:
        return []
    result = [[root.value]]
    level = [node for node in (root.left, root.right) if node]
    combinations = []
    while level:
        next_level = []
        for node in level:
            combinations.append(node.value)
            next_level += [node for node in (node.left, node.right) if node]
        next_iter = []
        while result:
            value = result.pop()
            for combination in permutations(combinations):
                next_iter.append(value + list(combination))
        result = next_iter
        level = next_level
    return result


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3]
        self.tree.head = self.tree.create(arr)
        self.assertEqual([[2, 1, 3], [2, 3, 1]], find_sequences(self.tree.head))
