# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"
import unittest


def func_one(string: str, length: int):
    string = string[:length]
    flag = 1
    while flag:
        flag = 0
        for index, char in enumerate(string):
            if char == ' ':
                string = string[:index] + '%20' + string[index + 1:]
                flag = 1
                break
    return string


def func_two(string: str, length: int):
    string = list(string[:length])
    for index, char in enumerate(string):
        if char == ' ':
            string[index] = '%20'
    return ''.join(string)


class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.func = func_two

    def test_one(self):
        self.assertEqual(self.func('Mr John Smith ', 13), 'Mr%20John%20Smith')


if __name__ == "__main__":
    unittest.main()
