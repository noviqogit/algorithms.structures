# Animal Shelter: An animal shelter, which holds only dogs and cats,
# operates on a strictly"first in, first out"basis.
# People must adopt either the "oldest" (based on arrival time) of all animal sat the shelter, or they can
# select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data structures to maintain
# this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
# You may use the built-in Linkedlist data structure.

import unittest
from exercises.LinkedList import implementation


class Solution:
    def __init__(self):
        self.queue = implementation.SingleLinkedList()

    def enqueue(self, item):
        self.queue.addAtTail(item)

    def dequeueAny(self, choice=None):
        node = self.queue.head
        if not node:
            return
        if not choice:
            result = node.value
            self.queue.deleteAtIndex(0)
            return result
        if node.value == choice:
            result = node.value
            self.queue.head = node.next
            return result
        prev, node = node, node.next
        while node:
            if node.value == choice:
                result = node.value
                prev.next = node.next
                return result
            prev, node = node, node.next

    def dequeueDog(self):
        return self.dequeueAny(choice='dog')

    def dequeueCat(self):
        return self.dequeueAny(choice='cat')


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Solution()
        items = ['cat', 'dog', 'cat', 'cat', 'dog', 'dog']
        for item in items:
            self.data.enqueue(item)

    def test_one(self):
        self.data.dequeueAny()
        self.data.dequeueCat()
        self.assertEqual(self.data.queue.view(), ['dog', 'cat', 'dog', 'dog'])

    def test_two(self):
        self.data.dequeueDog()
        self.data.dequeueAny()
        self.data.dequeueDog()
        self.assertEqual(self.data.queue.view(), ['cat', 'cat', 'dog'])

        if __name__ == "__main__":
            unittest.main()
