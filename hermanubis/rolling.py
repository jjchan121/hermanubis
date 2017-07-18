import pandas as pd
import numpy as np
from hermanubis.expressions import Expression


class Count(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Count, self).__init__(short_name='n', long_name='Count', desc='Rolling Count',
                                    periods=periods,
                                    *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_count(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Kurt(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Kurt, self).__init__(short_name='κ', long_name='Kurt', desc='Rolling Kurtosis',
                                   periods=periods,
                                   *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_kurt(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Max(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Max, self).__init__(short_name='H', long_name='Max', desc='Rolling Maxium',
                                  periods=periods,
                                  *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_max(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Min(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Min, self).__init__(short_name='L', long_name='Min', desc='Rolling Minimum',
                                  periods=periods,
                                  *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_min(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Mean(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Mean, self).__init__(short_name='μ', long_name='Mean', desc='Rolling Mean',
                                   periods=periods,
                                   *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_mean(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Median(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Median, self).__init__(short_name='ˉ', long_name='Median', desc='Rolling Median',
                                     periods=periods,
                                     *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_median(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Quantile(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Quantile, self).__init__(short_name='q', long_name='Quantile', desc='Rolling Quantile',
                                       periods=periods,
                                       *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_quantile(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Skew(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Skew, self).__init__(short_name='Ω', long_name='Skew', desc='Rolling Skew',
                                   periods=periods,
                                   *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_skew(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Sum(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Sum, self).__init__(short_name='∑', long_name='Sum', desc='Rolling Sum',
                                  periods=periods,
                                  *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_sum(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Stddev(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Stddev, self).__init__(short_name='s', long_name='Stddev', desc='Rolling Stddev',
                                     periods=periods,
                                     *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_std(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Var(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Var, self).__init__(short_name='V', long_name='Var', desc='Rolling Variance',
                                  periods=periods,
                                  *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_var(val, self.periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class Correlation(Expression):
    def __init__(self, lhs, rhs, periods, *args, **kwargs):
        super(Correlation, self).__init__(short_name='ρ', long_name='Correlation', desc='Rolling Correlation',
                                          periods=periods,
                                          *args, **kwargs)
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table):
        periods = self.periods
        lhs = self.lhs
        rhs = self.rhs
        lval = None
        rval = None

        if lhs is not None:
            lval = lhs.evaluate(table)

        if rhs is not None:
            rval = rhs.evaluate(table)

        return pd.rolling_corr(lval, rval, periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + "," + repr(self.rhs) + str(self.periods) + ")"


class Covariance(Expression):
    def __init__(self, lhs, rhs, periods, *args, **kwargs):
        super(Covariance, self).__init__(short_name='Ξ', long_name='Covariance', desc='Rolling Covariance',
                                         periods=periods,
                                         *args, **kwargs)
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self, table):
        periods = self.periods
        lhs = self.lhs
        rhs = self.rhs
        lval = None
        rval = None

        if lhs is not None:
            lval = lhs.evaluate(table)

        if rhs is not None:
            rval = rhs.evaluate(table)

        return pd.rolling_cov(lval, rval, periods)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + "," + repr(self.rhs) + str(self.periods) + ")"


class Prod(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(Prod, self).__init__(short_name='∏', long_name='Prod', desc='Rolling Product',
                                   periods=periods,
                                   *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        periods = self.periods
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_apply(val, periods, np.prod)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class CumProd(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(CumProd, self).__init__(short_name='ʄ', long_name='CumProd', desc='Rolling Cumulative Product',
                                      periods=periods,
                                      *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        periods = self.periods
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_apply(val, periods, np.cumprod)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"


class CumSum(Expression):
    def __init__(self, expr, periods, *args, **kwargs):
        super(CumSum, self).__init__(short_name='ʃ', long_name='CumSum', desc='Rolling Cumulative Sum',
                                     periods=periods,
                                     *args, **kwargs)
        self.expr = expr

    def evaluate(self, table):
        periods = self.periods
        expr = self.expr
        val = None
        if expr is not None:
            val = expr.evaluate(table)
        return pd.rolling_apply(val, periods, np.cumsum)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.lhs) + ", " + str(self.periods) + ")"
