from sort.core.unittest_helper import *

from .selection import sort_selection


class Test(TestCase):
    def test(self):
        Generator(self).try_with(sort_selection, INPUT, OUTPUT)
