from sort.core.unittest_helper import *

from .insertion import sort_insertion


class Test(TestCase):
    def test(self):
        Generator(self).try_with(sort_insertion, INPUT, OUTPUT)
