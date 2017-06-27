import unittest

# add comment here
import unittest

from tests.expressions_test import ExpressionTest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ExpressionTest))
    return test_suite

mySuit = suite()

runner = unittest.TextTestRunner()
runner.run(mySuit)
# creating a new test suite
newSuite = unittest.TestSuite()
