# String Compression: Implement a method to perform basic string compression
# using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).
import unittest


def func(string: str):
    string += ' '
    length = len(string)
    count = 1
    i = 1
    result = ''
    while i < length:
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += f'{string[i - 1]}{count}'
            count = 1
        i += 1
    return result


class TestFunc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(func('aabcccccaaa'), 'a2b1c5a3')

    def test_second(self):
        self.assertEqual(func('abcd'), 'a1b1c1d1')


if __name__ == "__main__":
    unittest.main()
