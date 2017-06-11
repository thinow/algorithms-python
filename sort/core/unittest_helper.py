from copy import copy
from unittest import TestCase

INPUT = [49, 32, 74, 79, 43, 31, 81, 64, 8, 71]
OUTPUT = [8, 31, 32, 43, 49, 64, 71, 74, 79, 81]


class Generator:
    def __init__(self, assertions: TestCase):
        self.assertions = assertions

    def try_with(self, algorithm, input, expected):
        # given
        array = copy(input)
        # when
        algorithm(array)
        # then
        self.assertions.assertEqual(array, expected)
