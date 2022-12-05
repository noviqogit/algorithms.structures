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
    while level:
        level, values = next_level(level)
        combinations = []
        for combination in permutations(values):
            combinations.append(list(combination))
        result = iter_result(result, combinations)
    return result


def iter_result(result, combinations):
    _result = []
    for value in result:
        for combination in combinations:
            _result.append(value + combination)
    return _result


def next_level(level):
    values = []
    _level = []
    for node in level:
        values.append(node.value)
        _level += [node for node in (node.left, node.right) if node]
    return _level, values


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBinarySearchTree()

    def test_one(self):
        arr = [1, 2, 3]
        self.tree.head = self.tree.create(arr)
        self.assertEqual([[2, 1, 3], [2, 3, 1]], find_sequences(self.tree.head))
