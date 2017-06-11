from sort.core.unittest_helper import *

from .insertion import insertion


class Test(TestCase):
    def test(self):
        Generator(self).try_with(insertion, INPUT, OUTPUT)
