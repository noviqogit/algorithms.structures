class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None

    def view(self):
        _arr = []
        _node = self.head

        def recursion(arr, node):
            if not node:
                return
            recursion(arr, node.left)
            arr.append(node.value)
            recursion(arr, node.right)
            return node

        recursion(_arr, _node)
        return _arr
