# List of Depths: Given a binary tree, design an algorithm which creates
# a linked list of all the nodes at each depth (e.g., if you have a tree
# with depth D, you'll have D linked lists).

import unittest
from exercises.LinkedList.implementation import SingleLinkedList
from implementation import BinaryTree


def func(root):
    s = [root]
    lists = []
    while s:
        _next = []
        _list = SingleLinkedList()
        for node in s:
            _list.addAtTail(node.value)
            if node.left:
                _next.append(node.left)
            if node.right:
                _next.append(node.right)
        lists.append(_list)
        s = _next
    return lists


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree()

    def test_one(self):
        arr = [3, 2, 4, '#', '#', '#', 5, 7, '#', '#', 6, '#', '#']
        head = self.tree.create_preorder(arr)
        lists = func(head)
        self.assertEqual([[3], [2, 5], [4, 7, 6]], [_list.view() for _list in lists])
