# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?
import unittest


def func(mat: list[list]):
    n = len(mat)
    new = [[] for _ in range(n)]
    while mat:
        column = mat.pop(0)[::-1]
        for i in range(n):
            new[i].append(column[i])
    return new


class TestFunc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(func([[1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]),
                         [[3, 6, 9],
                          [2, 5, 8],
                          [1, 4, 7]])


if __name__ == "__main__":
    unittest.main()
