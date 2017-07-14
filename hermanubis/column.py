from hermanubis.expressions import Expression
import pandas as pd

class Column(Expression):
    def __init__(self, name, short_name=None):
        super(Column, self).__init__(short_name=short_name, long_name=name, desc='Column %s' % name)
        self.name = name

    def evaluate(self, table):
        name = self.name
        if isinstance(table, pd.Panel):
            if name in table.items:
                return table.loc[self.name, :, :]
            elif name in table.major_axis:
                return table.loc[:, self.name, :]
            elif name in table.minor_axis:
                return table.loc[:, :, self.name]
            else:
                return None
        elif isinstance(table, pd.DataFrame):
            return table[self.name]
        else:
            raise RuntimeError("%s type is not support as table in %s.evaluate" % (type(table), self.__class__))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.name.lower()
