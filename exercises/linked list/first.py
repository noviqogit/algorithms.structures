# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
from implementation import SingleLinkedList
import unittest


class Solution(SingleLinkedList):

    def remove_dups(self):
        prev = self.head
        arr = {prev.value, }
        node = prev.next
        while node:
            if node.value not in arr:
                arr.add(node.value)
                prev = node
            elif node.next:
                prev.next = node.next
            else:
                prev.next = None
                break
            node = prev.next

    def remove_dups_b(self):
        head = self.head
        while head:
            prev = head
            node = prev.next
            while node:
                if node.value == head.value:
                    if node.next:
                        prev.next = node.next
                    else:
                        prev.next = None
                        break
                else:
                    prev = prev.next
                node = prev.next
            head = head.next


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()
        self.func = self.data.remove_dups_b

    def test_one(self):
        nodes = [1, 1, 1, 1, 1]
        for node in nodes:
            self.data.addAtTail(node)
        self.func()
        self.assertEqual(self.data.view(), [1])

    def test_two(self):
        nodes = [4, 3, 2, 3, 3, 2]
        for node in nodes:
            self.data.addAtTail(node)
        self.func()
        self.assertEqual(self.data.view(), [4, 3, 2])

    def test_three(self):
        nodes = [1, 2, 3, 4, 5]
        for node in nodes:
            self.data.addAtTail(node)
        self.func()
        self.assertEqual(self.data.view(), [1, 2, 3, 4, 5])

    def test_four(self):
        nodes = [1]
        for node in nodes:
            self.data.addAtTail(node)
        self.func()
        self.assertEqual(self.data.view(), [1])


if __name__ == "__main__":
    unittest.main()
