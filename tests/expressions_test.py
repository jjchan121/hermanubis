
import unittest
# from unittest import TestCase
import pandas as pd
import numpy as np
from hermanubis.column import Column
from hermanubis.expressions import  Greater

class ExpressionTest(unittest.TestCase):
    def setup(self):
        self.two_cols_df = pd.DataFrame({"A" : np.linspace(0, 19, 20),
                                         "B" : np.linspace(-19,0, 20)})

        self.two_cols_rand_df = pd.DataFrame({"A" : np.random.normal(0, 1, 20),
                                              "B" : np.random.normal(0, 1, 20)})

    def test_greater(self):
        self.setup()
        df = self.two_cols_rand_df
        a = Column("A")
        b = Column("B")
        gt = Greater(a, b)
        res = gt.evaluate(df)
        target = df['A'] > df['B']
        self.__np_assert_almost_equal(res.values, target.values)

        gt2 = a > b
        res2 = gt2.evaluate(df)
        self.__np_assert_almost_equal(res2.values, target.values)




    def __np_assert_almost_equal(self, target, output, precision=10):
        try:
            np.testing.assert_almost_equal(target, output, precision)
        except AssertionError as e:
            self.fail(e.message)



