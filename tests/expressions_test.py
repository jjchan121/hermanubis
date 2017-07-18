
import unittest
# from unittest import TestCase
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
from hermanubis.column import Column
from hermanubis.constant import Constant
from hermanubis.expressions import Greater

class ExpressionTest(unittest.TestCase):

    @staticmethod
    def create_mi_df():
        inst_id = [ i % 4 for i in range(20)]
        t0 = datetime.datetime(2010,1,1,0,0,0)

        def ts_generator(t0, inst_id, on_label):
            i = 0
            for s in inst_id:
                yield t0 + timedelta(days=i)
                if s == on_label:
                    i = i + 1

        ts = list(ts_generator(t0, inst_id, 3))
        multi_index = pd.MultiIndex.from_arrays([ts, inst_id])

        data = np.random.normal(100,1, 100).reshape(20,5)
        return pd.DataFrame(data=data, index=multi_index, columns=['A', 'B', 'C', 'D', 'E'])

    def setup(self):
        self.two_cols_df = pd.DataFrame({"A" : np.linspace(0, 19, 20),
                                         "B" : np.linspace(-19,0, 20)})

        self.two_cols_rand_df = pd.DataFrame({"A" : np.random.normal(0, 1, 20),
                                              "B" : np.random.normal(0, 1, 20)})

        self.midf = ExpressionTest.create_mi_df()

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



    def test_constants(self):
        self.setup()
        midf = self.midf

        a = Column("A")
        gt100 = a > Constant(100.0)
        gt100_res = gt100.evaluate(midf)

        df = midf.xs('A', axis=1).unstack()
        target = df > 100.0
        self.__np_assert_almost_equal(target.values, gt100_res.values)


    def __np_assert_almost_equal(self, target, output, precision=10):
        try:
            np.testing.assert_almost_equal(target, output, precision)
        except AssertionError as e:
            self.fail(e.message)



