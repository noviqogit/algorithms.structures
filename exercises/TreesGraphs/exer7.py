# Build Order: You are given a list of projects and a list of dependencies
# (which is a list of pairs of projects, where the second project is dependent on the first project).
# All of a project's dependencies must be built before the project is. Find a build order that
# will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, e), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

import unittest


class Solution:
    def func(self, projects, dependencies):
        graph = self.create_graph(dependencies)
        for node in graph.keys():
            path = self.check_path(node, graph, projects)
            if path:
                return path
        return False

    def create_graph(self, dependencies):
        graph = {}
        for nodes in dependencies:
            if nodes[0] not in graph:
                graph[nodes[0]] = [nodes[1]]
            else:
                graph[nodes[0]].append(nodes[1])
        return graph

    def check_path(self, node, graph, projects):
        _projects = projects.copy()
        _projects.discard(node)
        if not _projects:
            return [node]
        if node not in graph or not graph[node]:
            return False
        for subnode in graph[node]:
            _next = self.check_path(subnode, graph, _projects)
            if _next:
                return [node] + _next
        return False


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one(self):
        projects = {'a', 'b', 'c', 'd', 'e', 'f'}
        dependencies = [('a', 'd'), ('f', 'e'), ('e', 'b'), ('f', 'b'), ('b', 'a'), ('f', 'a'), ('d', 'c')]
        result = self.solution.func(projects, dependencies)
        self.assertEqual(['f', 'e', 'b', 'a', 'd', 'c'], result)

    def test_two(self):
        projects = {'a', 'b', 'c', 'd', 'e', 'f'}
        dependencies = [('a', 'd'), ('e', 'b'), ('f', 'b'), ('b', 'a'), ('f', 'a'), ('d', 'c')]
        result = self.solution.func(projects, dependencies)
        self.assertFalse(result)
