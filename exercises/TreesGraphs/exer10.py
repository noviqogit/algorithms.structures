# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree
# of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

import unittest
from implementation import BinaryTree


def find_root(t1, root) -> list:
    """
    return roots from t1 which have same values like root from t2
    """
    pass


def is_subtree(root1, root2):
    if not root2:
        return True
    if not root1 and root2 or root1.value != root2.value:
        return False
    return is_subtree(root1.left, root2.left) and is_subtree(root1.right, root2.right)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.t1 = BinaryTree()
        self.t2 = BinaryTree()

    def test_one(self):
        # for t1 in find_root(t1, root)
        t1 = [3, 2, '#', '#', 5, 4, '#', '#', 6, '#', '#']
        self.t1.create_preorder(t1)
        t2 = [3, 2, '#', '#', 5, '#', '#']
        self.t2.create_preorder(t2)
        self.assertTrue(is_subtree(self.t1.head, self.t2.head))

    def test_two(self):
        # for t1 in find_root(t1, root)
        t1 = [3, 2, '#', '#', 5, 4, '#', '#', 6, '#', '#']
        self.t1.create_preorder(t1)
        t2 = [3, 2, '#', '#', 6, '#', '#']
        self.t2.create_preorder(t2)
        self.assertFalse(is_subtree(self.t1.head, self.t2.head))
