import unittest
from copy import copy

from sort import sort


class Generator:
    def __init__(self, assertions):
        self.assertions = assertions

    def try_with(self, algorithm, input, expected):
        # given
        array = copy(input)
        # when
        algorithm(array)
        # then
        self.assertions.assertEqual(array, expected)


class TestSort(unittest.TestCase):
    def setUp(self):
        self.generator = Generator(self)

    def test_empty(self):
        self.generator.try_with(
            algorithm=sort.insertion,
            input=[],
            expected=[]
        )

    def test_single_value(self):
        self.generator.try_with(
            algorithm=sort.insertion,
            input=[1],
            expected=[1]
        )

    def test_two_values(self):
        self.generator.try_with(
            algorithm=sort.insertion,
            input=[1, 2],
            expected=[1, 2]
        )

    def test_insertion(self):
        self.generator.try_with(
            algorithm=sort.insertion,
            input=[49, 32, 74, 79, 43, 31, 81, 64, 8, 71],
            expected=[8, 31, 32, 43, 49, 64, 71, 74, 79, 81]
        )
