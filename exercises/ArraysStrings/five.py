# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false

from collections import Counter
import unittest


def func(s1: str, s2: str):
    d = Counter(s1 + s2)
    actions = 0
    for value in d.values():
        if actions > 1:
            return False
        if value == 1:
            actions += 1
    return True


class TestFunc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(func('pale', 'ple'), True)

    def test_second(self):
        self.assertEqual(func('pales', 'pale'), True)

    def test_third(self):
        self.assertEqual(func('pale', 'bale'), True)

    def test_fourth(self):
        self.assertEqual(func('pale', 'bake'), False)


if __name__ == "__main__":
    unittest.main()
