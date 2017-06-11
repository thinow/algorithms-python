from sort.core.unittest_helper import *

from .shell import sort_shell


class Test(TestCase):
    def test(self):
        Generator(self).try_with(sort_shell, INPUT, OUTPUT)
