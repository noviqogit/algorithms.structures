class Node:
    def __init__(self, val):
        self.next = None
        self.value = val


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.value

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            new = Node(val)
            node = self.head
            while node.next:
                node = node.next
            node.next = new
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            new = Node(val)
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new.next = node.next
            node.next = new
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            node.next = node.next.next
        self.size -= 1


class DoubleNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.value = val


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.value

    def addAtHead(self, val: int) -> None:
        new = DoubleNode(val)
        new.next = self.head
        if self.size > 0:
            self.head.prev = new
        self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            new = DoubleNode(val)
            node = self.head
            while node.next:
                node = node.next
            node.next = new
            new.prev = node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        if index == self.size:
            self.addAtTail(val)
        else:
            new = DoubleNode(val)
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new.prev = node
            new.next = node.next
            node.next.prev = new
            node.next = new
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        elif index == 0:
            if self.size == 1:
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            if index == self.size - 1:
                node.next = None
            else:
                node.next.next.prev = node
                node.next = node.next.next
        self.size -= 1
