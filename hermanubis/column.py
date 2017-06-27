from hermanubis.expressions import Expression
import pandas as pd

class Column(Expression):
    def __init__(self, name, short_name=None):
        super(Column, self).__init__(short_name=short_name, long_name=name, desc='Column %s' % name)
        self.name = name

    def evaluate(self, table):
        if isinstance(table, pd.Panel):
            return table.loc[:, :, self.name]
        elif isinstance(table, pd.DataFrame):
            return table[self.name]
        else:
            raise NotImplementedError

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.name.lower()
