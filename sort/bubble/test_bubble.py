from sort.core.unittest_helper import *

from .bubble import bubble


class Test(TestCase):
    def test(self):
        Generator(self).try_with(bubble, INPUT, OUTPUT)
