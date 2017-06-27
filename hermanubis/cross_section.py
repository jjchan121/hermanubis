
import pandas as pd
import numpy as np
from hermanubis.expressions import Expression

class Abs(Expression):
    def __init__(self, expr, *args, **kwargs):
        super(Abs, self).__init__(short_name='|', long_name='Abs', desc='Cross section Abs',
                                  *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)

            if isinstance(val, pd.Panel):
                return val.apply(np.abs, axis='major')
            elif isinstance(val, pd.DataFrame) or isinstance(val, pd.Series):
                return val.apply(np.abs)
            else:
                raise NotImplementedError


    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + ")"



class Average(Expression):
    def __init__(self, expr, *args, **kwargs):
        super(Average, self).__init__(short_name='|', long_name='Average', desc='Cross section Average',
                                  *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)

            if isinstance(val, pd.Panel):
                return val.apply(np.average, axis='major')
            elif isinstance(val, pd.DataFrame):
                return val.apply(np.average, axis=1)
            # elif isinstance(val, pd.Series):
            #     return val.apply(np.average)
            else:
                raise NotImplementedError


    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + ")"



class Rank(Expression):
    def __init__(self, expr, ascending=True, *args, **kwargs):
        super(Rank, self).__init__(short_name='R', long_name='Rank', desc='Cross section rank',
                                   *args, **kwargs)
        self.ascending = ascending
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        df = None

        if expr is not None:
            df = expr.evaluate(table)
        else:
            if isinstance(table, pd.DataFrame):
                df = table

        if isinstance(df, pd.DataFrame):
            rank = df.rank(axis=1)/(df.shape[1]-1)
            return rank
        else:
            raise Exception("Only Pandas DataFrame is supported for Rank")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + ")"
