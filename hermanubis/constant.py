from hermanubis.expressions import Expression
import pandas as pd


class Constant(Expression):
    def __init__(self, val, short_name=None):
        super(Constant, self).__init__(short_name=short_name, long_name=short_name, desc='Constant %s' % short_name)
        self.val = val

    def evaluate(self, table):
        return self.val

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.val)
