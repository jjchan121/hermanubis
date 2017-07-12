import pandas as pd
import numpy as np
from hermanubis.expressions import Expression


class Count(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Count, self).__init__(short_name='n', long_name='Count', desc='Rolling Count',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_count(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Kurt(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Kurt, self).__init__(short_name='κ', long_name='Kurt', desc='Rolling Kurtosis',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_kurt(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Max(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Max, self).__init__(short_name='H', long_name='Max', desc='Rolling Maxium',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_max(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Min(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Min, self).__init__(short_name='L', long_name='Min', desc='Rolling Minimum',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_min(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Mean(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Mean, self).__init__(short_name='μ', long_name='Mean', desc='Rolling Mean',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_mean(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Median(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Median, self).__init__(short_name='ˉ', long_name='Median', desc='Rolling Median',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_median(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Quantile(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Quantile, self).__init__(short_name='q', long_name='Quantile', desc='Rolling Quantile',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_quantile(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Skew(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Skew, self).__init__(short_name='Ω', long_name='Skew', desc='Rolling Skew',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_skew(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Sum(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Sum, self).__init__(short_name='∑', long_name='Sum', desc='Rolling Sum',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_sum(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Stddev(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Stddev, self).__init__(short_name='s', long_name='Stddev', desc='Rolling Stddev',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_std(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Var(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Var, self).__init__(short_name='V', long_name='Var', desc='Rolling Variance',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_var(val, self.window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class Correlation(Expression):
    def __init__(self, lhs, rhs, window, *args, **kwargs):
        super(Correlation, self).__init__(short_name='ρ', long_name='Correlation', desc='Rolling Correlation',
                *args, **kwargs)
        self.lhs = lhs
        self.window = window

    def evaluate(self, table):
        window = self.window
        lhs = self.lhs
        rhs = self.rhs
        lval = None
        rval = None

        if lhs is not None:
            lval = lhs.evaluate(table)

        if rhs is not None:
            rval = rhs.evaluate(table)

        return pd.rolling_corr(lval, rval, window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + "," + repr(self.rhs) + str(self.window) + ")"


class Covariance(Expression):
    def __init__(self, lhs, rhs, window, *args, **kwargs):
        super(Covariance, self).__init__(short_name='Ξ', long_name='Covariance', desc='Rolling Covariance',
                *args, **kwargs)
        self.lhs = lhs
        self.window = window

    def evaluate(self, table):
        window = self.window
        lhs = self.lhs
        rhs = self.rhs
        lval = None
        rval = None

        if lhs is not None:
            lval = lhs.evaluate(table)

        if rhs is not None:
            rval = rhs.evaluate(table)

        return pd.rolling_cov(lval, rval, window)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + "," + repr(self.rhs) + str(self.window) + ")"


class Prod(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(Prod, self).__init__(short_name='∏', long_name='Prod', desc='Rolling Product',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        window = self.window
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_apply(val, window, np.prod)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class CumProd(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(CumProd, self).__init__(short_name='ʄ', long_name='CumProd', desc='Rolling Cumulative Product',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        window = self.window
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_apply(val, window, np.cumprod)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"


class CumSum(Expression):
    def __init__(self, expr, window, *args, **kwargs):
        super(CumSum, self).__init__(short_name='ʃ', long_name='CumSum', desc='Rolling Cumulative Sum',
            *args, **kwargs)
        self.expr = expr
        self.window = window

    def evaluate(self, table):
        window = self.window
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_apply(val, window, np.cumsum)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.window) + ")"

