from sort.core.unittest_helper import *

from .merge import merge
from .merge import sort_merge


class Test(TestCase):
    def test_merge_function(self):
        self.assertEqual(merge([1, 3, 4], [2, 5]), [1, 2, 3, 4, 5])

    def test_sort_merge(self):
        result = sort_merge(INPUT)
        self.assertEqual(result, OUTPUT)
