from unittest.case import TestCase

from complexity.matrix.matrix import sum_two_dimension, sum_one_dimension

EXPECTED_SUM = 16


class Test(TestCase):
    def test_two_dimension(self):
        # given
        matrix = [
            [None, None, 1],
            [2, None, 5],
            [0, 8, None]
        ]

        # when
        sum = sum_two_dimension(matrix)

        # then
        self.assertEqual(sum, EXPECTED_SUM)

    def test_one_dimension(self):
        # given
        matrix = [
            (0, 2, 1),
            (1, 0, 2),
            (1, 2, 5),
            (2, 0, 0),
            (2, 1, 8)
        ]

        # when
        sum = sum_one_dimension(matrix)

        # then
        self.assertEqual(sum, EXPECTED_SUM)
