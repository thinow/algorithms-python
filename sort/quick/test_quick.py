from sort.core.unittest_helper import *

from .quick import sort_quick


class Test(TestCase):
    def test(self):
        Generator(self).try_with(sort_quick, INPUT, OUTPUT)
