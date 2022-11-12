# Palindrome Permutation: Given a string, write a function to check
# if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

from collections import Counter
import unittest


def func(string: str):
    count = 0
    string = string.lower()
    d = Counter(string)
    length = len(min(string.split()))
    for value in d.values():
        count += value // 2
    if count >= length:
        return True
    return False


class TestFunc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(func('Tact Coa'), True)

    def test_second(self):
        self.assertEqual(func('Tact Baa'), False)


if __name__ == "__main__":
    unittest.main()
