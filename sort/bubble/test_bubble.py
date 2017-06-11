from sort.core.unittest_helper import *

from .bubble import sort_bubble


class Test(TestCase):
    def test(self):
        Generator(self).try_with(sort_bubble, INPUT, OUTPUT)
