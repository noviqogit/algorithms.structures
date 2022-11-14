# Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

import unittest
from queue import Queue


def has_route(graph, start, end):
    queue = Queue()
    queue.put(start)
    finished = set()
    while queue.qsize():
        node = queue.get()
        routes = graph[node]
        for route in routes:
            if route == end:
                return True
            if route in finished:
                continue
            finished.add(node)
            queue.put(route)
    return False


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = {0: (1,), 1: (2,), 2: (0, 3), 3: (2,), 4: (6,), 5: (4,), 6: (5,), 7: (3,)}
        self.func = has_route

    def test_one(self):
        self.assertEqual(self.func(self.graph, 0, 3), True)

    def test_two(self):
        self.assertEqual(self.func(self.graph, 0, 7), False)
