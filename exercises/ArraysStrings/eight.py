# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.
import unittest


def func(mat: list[list]):
    lines, columns = [], []
    M = range(len(mat))
    N = range(len(mat[0]))
    for i in M:
        for j in N:
            if mat[i][j] == 0:
                lines.append(i)
                columns.append(j)
    for i in lines:
        mat[i] = [0 for _ in N]
    for j in columns:
        for i in M:
            mat[i][j] = 0
    return mat


class TestFunc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(func(
            [[1, 2, 3],
             [4, 0, 6],
             [7, 8, 9]]),

            [[1, 0, 3],
             [0, 0, 0],
             [7, 0, 9]])

    def test_second(self):
        self.assertEqual(func(
            [[1, 2, 0],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12]]),

            [[0, 0, 0],
             [4, 5, 0],
             [7, 8, 0],
             [10, 11, 0]])

    def test_third(self):
        self.assertEqual(func(
            [[1, 2, 3, 10],
             [4, 5, 0, 11],
             [7, 8, 9, 12]]),

            [[1, 2, 0, 10],
             [0, 0, 0, 0],
             [7, 8, 0, 12]])


if __name__ == "__main__":
    unittest.main()
