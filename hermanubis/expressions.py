
# import hermanubis.arithmetic_operator as op
from enum import Enum
import pandas as pd

class CalcMode(Enum):
    BATCH = 1
    ONLINE = 2

class SequentialMode(Enum):
    OFF = 1
    ON = 2

class Expression(object):
    def __init__(self, short_name=None, long_name=None, desc=None,
                 calc_mode=CalcMode.BATCH, seq_mode = SequentialMode.OFF, *args, **kwargs):
        self.short_name = short_name
        self.long_name = long_name
        self.desc = desc
        self.calc_mode = calc_mode
        self.seq_mode = seq_mode

    def evaluate(self, table, *args, **kwargs):
        raise NotImplementedError

    def __call__(self, obj, *args, **kwargs):
        return self.evaluate(obj, *args, **kwargs)

    def __add__(self, other):
        return Plus(self, other)

    def __radd__(self, other):
        return Plus(other, self)

    def __sub__(self, other):
        return Minus(self, other)

    def __rsub__(self, other):
        return Minus(other, self)

    def __mul__(self, other):
        return Multiply(self, other)

    def __rmul__(self, other):
        return Multiply(other, self)

    def __truediv__(self, other):
        return Divide(self, other)

    def __rtruediv__(self, other):
        return Divide(other, self)

    def __gt__(self, other):
        return Greater(self, other)

    # def __lt__(self, other):


class Plus(Expression):
    def __init__(self, lhs=None, rhs=None, *args, **kwargs):
        super(Plus, self).__init__(short_name='+', long_name='Plus', desc='Plus')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval + rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)


class Minus(Expression):
    def __init__(self, lhs=None, rhs=None):
        super(Minus, self).__init__(short_name='-', long_name='Minus', desc='Minus')
        self.lhs = lhs
        self.rhs = rhs

    @staticmethod
    def minus_on_unequal_shape(df1, df2):
        arr1 = df1.values
        arr2 = df2.values
        val = None

        if len(arr1.shape) == 1 or arr1.shape[1] == 1:
            val = arr1[:,None] - arr2
            out_df = pd.DataFrame(val, index=df2.index)
            out_df.columns = df2.columns
        elif len(arr2.shape) ==1 or arr2.shape[1] == 1:
            val = arr1 - arr2[:,None]
            out_df = pd.DataFrame(val, index=df1.index)
            out_df.columns = df1.columns
        else:
            raise ArithmeticError

        return out_df

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        if lval.shape == rval.shape:
            return lval - rval
        else:
            return Minus.minus_on_unequal_shape(lval, rval)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)



class Multiply(Expression):
    def __init__(self, lhs=None, rhs=None):
        super(Multiply, self).__init__(short_name='*', long_name='Multiply', desc='Multiply')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval * rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)


class Divide(Expression):
    def __init__(self, lhs=None, rhs=None):
        super(Divide, self).__init__(short_name='/', long_name='Divide', desc='Divide')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval / rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)


class Greater(Expression):
    def __init__(self, lhs=None, rhs=None, *args, **kwargs):
        super(Greater, self).__init__(short_name='>', long_name='Greater', desc='Greater')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval > rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)


class GreaterOrEqual(Expression):
    def __init__(self, lhs=None, rhs=None, *args, **kwargs):
        super(GreaterOrEqual, self).__init__(short_name='≥', long_name='Greater', desc='Greater')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval >= rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)


class Lesser(Expression):
    def __init__(self, lhs=None, rhs=None, *args, **kwargs):
        super(Lesser, self).__init__(short_name='<', long_name='Lesser', desc='Lesser')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval < rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)


class LesserOrEqual(Expression):
    def __init__(self, lhs=None, rhs=None, *args, **kwargs):
        super(LesserOrEqual, self).__init__(short_name='≤', long_name='Lesser Or Equal', desc='Lesser Or Equal')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval <= rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)



class ElemwiseEqual(Expression):
    def __init__(self, lhs=None, rhs=None, *args, **kwargs):
        super(ElemwiseEqual, self).__init__(short_name='=', long_name='ElemwiseEqual', desc='ElemwiseEqual')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval == rval

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)


class ElemwiseNotEqual(Expression):
    def __init__(self, lhs=None, rhs=None, *args, **kwargs):
        super(ElemwiseNotEqual, self).__init__(short_name='≠', long_name='ElemwiseNotEqual', desc='ElemwiseNotEqual')
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table, *args, **kwargs):
        lval = self.lhs.evaluate(table, *args, **kwargs)
        rval = self.rhs.evaluate(table, *args, **kwargs)
        return lval != rval

    def __str__(self):
            return self.__repr__()

    def __repr__(self):
        return repr(self.lhs) + self.short_name + repr(self.rhs)

