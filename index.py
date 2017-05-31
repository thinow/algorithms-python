import unittest
import sort.test_insertion
suite = unittest.TestLoader().loadTestsFromModule(sort.test_insertion)
unittest.TextTestRunner().run(suite)
