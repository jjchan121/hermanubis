import unittest

# add comment here
import unittest

from tests.expressions_test import ExpressionTest
from tests.conditions_test import ConditionTest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ExpressionTest))
    test_suite.addTest(unittest.makeSuite(ConditionTest))
    return test_suite

mySuit = suite()

runner = unittest.TextTestRunner()
runner.run(mySuit)
# creating a new test suite
newSuite = unittest.TestSuite()
