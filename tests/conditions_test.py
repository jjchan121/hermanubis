
import unittest
# from unittest import TestCase
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
from hermanubis.constant import Constant
from hermanubis.column import Column
from hermanubis.conditions import IfElse
from hermanubis.expressions import Greater

class ConditionTest(unittest.TestCase):
    def setup(self):

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

        data = np.random.normal(100, 1, 100).reshape(20,5)
        df = pd.DataFrame(data=data, index=multi_index, columns=['A', 'B', 'C', 'D', 'E'])
        self.df = df

    def test(self):
        self.setup()
        df = self.df

        colA = Column("A")
        colB = Column("B")
        colC = Column("C")

        cond = IfElse(colA > Constant(100.0), Constant(2), Constant(0.5))

        cond_data = cond.evaluate(df)

        # calc the target
        arrA = np.copy(df['A'].values)
        arrB = df['B'].values
        arrC = df['C'].values

        pred = arrA > 100.0
        arrA[pred] = 2.0
        arrA[np.logical_not(pred)] = 0.5
        self.__np_assert_almost_equal(arrA, cond_data.values.transpose(), 5)



    def __np_assert_almost_equal(self, target, output, precision=10):
        try:
            np.testing.assert_almost_equal(target, output, precision)
        except AssertionError as e:
            self.fail(e)


