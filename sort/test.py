import unittest

from sort import sort

INPUT = [2, 5, 1, 3, 4]
EXPECTED = [1, 2, 3, 4, 5]


class TestSort(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(sort.insertion(INPUT), EXPECTED)
