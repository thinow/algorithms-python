from unittest.case import TestCase

from complexity.alphabet.alphabet import count_with_all_letters, count_on_the_fly

INPUT = ['A', 'D', 'N', 'Z', 'U', 'A', 'Z', 'F', 'F', 'A', 'P', 'S', 'D']
EXPECTED = {
    'A': 3,
    'D': 2,
    'F': 2,
    'N': 1,
    'P': 1,
    'S': 1,
    'U': 1,
    'Z': 2
}


class Test(TestCase):
    def test_on_the_fly(self):
        # when
        result = count_on_the_fly(INPUT)

        # then
        self.assertEqual(result, EXPECTED)

    def test_loop_all_letters(self):
        # when
        result = count_with_all_letters(INPUT)

        # then
        self.assertEqual(result, EXPECTED)
