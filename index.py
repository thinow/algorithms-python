import os
import unittest

start_dir = os.path.dirname(__file__)
suite = unittest.TestLoader().discover(start_dir)
unittest.TextTestRunner().run(suite)
