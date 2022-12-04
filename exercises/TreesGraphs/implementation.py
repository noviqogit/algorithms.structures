class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def view(self):
        return self.recr(self.head)

    def recr(self, node):
        if not node:
            return []
        return self.recr(node.left) + [node.value] + self.recr(node.right)
