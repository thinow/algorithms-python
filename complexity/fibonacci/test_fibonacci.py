from unittest.case import TestCase

from complexity.fibonacci import fibonacci


class Test(TestCase):
    def test_sequence(self):
        self.assertEqual(fibonacci.get(0), 0)
        self.assertEqual(fibonacci.get(1), 1)
        self.assertEqual(fibonacci.get(2), 1)
        self.assertEqual(fibonacci.get(3), 2)
        self.assertEqual(fibonacci.get(4), 3)
        self.assertEqual(fibonacci.get(5), 5)
        self.assertEqual(fibonacci.get(6), 8)
        self.assertEqual(fibonacci.get(7), 13)
        self.assertEqual(fibonacci.get(8), 21)
