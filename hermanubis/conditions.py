import pandas as pd
import theano
from theano import tensor as T
from theano.ifelse import ifelse
from hermanubis.expressions import Expression


p = T.bmatrix('p')
te = T.fmatrix('te')
fe = T.fmatrix('fe')

out = ifelse(p, te, fe)

ifelse_fn = theano.function([p, te, fe], outputs=out, mode=theano.Mode(linker='vm'))

class IfElse(Expression):
    def __init__(self, predicate, true_exp, else_exp, *args, **kwargs):
        super(IfElse, self).__init__(short_name='i', long_name='IfElse', desc='IfElse',
                                    *args, **kwargs)
        self.predicate = predicate
        self.true_exp = true_exp
        self.false_exp = else_exp

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

