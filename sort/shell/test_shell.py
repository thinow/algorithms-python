from sort.core.unittest_helper import *

from .shell import shell


class Test(TestCase):
    def test(self):
        Generator(self).try_with(shell, INPUT, OUTPUT)
