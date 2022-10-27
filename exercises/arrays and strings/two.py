# Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.

from collections import defaultdict
import unittest


def func(str1: str, str2: str):
    if not len(str1) == len(str2):
        return False
    d = defaultdict(int)
    for char in str1:
        d[char] += 1
    for _char in str2:
        d[_char] -= 1
        if d[_char] < 0:
            return False
    return True


class TestFunc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(func('', 'a'), False)

    def test_second(self):
        self.assertEqual(func('aab', 'aab'), True)

    def test_third(self):
        self.assertEqual(func('abcd', 'dbca'), True)

    def test_fourth(self):
        self.assertEqual(func('abcdD', 'abcdd'), False)


if __name__ == "__main__":
    unittest.main()
