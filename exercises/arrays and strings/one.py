# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

from collections import defaultdict
import unittest


def func_one(string: str):
    if not string:
        return False
    d = defaultdict(int)
    for char in string.lower():
        d[char] += 1
        if d[char] > 1:
            return False
    return True


def func_two(string: str):
    if not string:
        return False
    length = len(string)
    if length == 1:
        return True
    string = sorted(string.lower())
    i = 1
    while i < length:
        if string[i - 1] == string[i]:
            return False
        i += 1
    return True


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.func = func_two

    def test_empty(self):
        self.assertEqual(self.func(''), False)

    def test_one(self):
        self.assertEqual(self.func('A'), True)

    def test_second(self):
        self.assertEqual(self.func('aA'), False)

    def test_third(self):
        self.assertEqual(self.func('abcd'), True)

    def test_fourth(self):
        self.assertEqual(self.func('abcdD'), False)


if __name__ == "__main__":
    unittest.main()
