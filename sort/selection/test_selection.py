from sort.core.unittest_helper import *

from .selection import selection


class Test(TestCase):
    def test(self):
        Generator(self).try_with(selection, INPUT, OUTPUT)
