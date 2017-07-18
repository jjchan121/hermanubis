import pandas as pd
import numpy as np
from hermanubis.expressions import Expression

class FuncWrapper(Expression):
    def __init__(self, expr, func, *args, **kwargs):
        super(FuncWrapper, self).__init__(*args, **kwargs)
        self.expr = expr
        self.func = func

    def evaluate(self, table, *args, **kwargs):
        expr = self.expr
        func = self.func
        val = None
        if expr is not None:
            val = expr.evaluate(table, *args, **kwargs)
            return val.apply(func, *args, **kwargs)
        else:
            raise NotImplementedError

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + ")"



