import pandas as pd
import numpy as np
from hermanubis.expressions import Expression

class Delay(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Delay, self).__init__(short_name='d', long_name='Delay', desc='Delay',
                                      *args, **kwargs)
        self.expr = expr
        self.periods = periods

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)

            if isinstance(val, pd.Panel) or isinstance(val, pd.DataFrame) or isinstance(val, pd.Series):
                return val.shift(self.periods)
            else:
                raise NotImplementedError

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + "," + repr(self.periods) + ")"



class Delta(Expression):
    def __init__(self, expr, periods, fillna_val=None, *args, **kwargs):
        super(Delta, self).__init__(short_name='d', long_name='Delta', desc='Delta',
                                    *args, **kwargs)
        self.expr = expr
        self.periods = periods
        self.fillna_val = fillna_val

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)

            if isinstance(val, pd.Panel) or isinstance(val, pd.DataFrame) or isinstance(val, pd.Series):
                out = val.diff(self.periods)
                if self.fillna_val is not None:
                    out = out.fillna(self.fillna_val)
                    return out
                else:
                    return out
            else:
                raise NotImplementedError

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + ", " + repr(self.periods) + ")"
