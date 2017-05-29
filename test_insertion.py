import unittest
from insertion import sort


class TestSortInsertion(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort([2, 5, 1, 3, 4]), [1, 2, 3, 4, 5])
