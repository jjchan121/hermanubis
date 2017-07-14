import numpy as np
import pandas as pd
import theano
from builtins import isinstance
from theano import tensor as T
from theano.ifelse import ifelse
from hermanubis.expressions import Expression

# theano.config.compute_test_value = 'off'


# p = T.fmatrix('p')
# te = T.fmatrix('te')
# fe = T.fmatrix('fe')
#
# out = ifelse(p, te, fe)
# out = T.switch(p, te, fe)

# ifelse_fn = theano.function([p, te, fe], outputs=out, mode=theano.Mode(linker='vm'))
# ifelse_fn = theano.function([p, te, fe], outputs=out)

class IfElse(Expression):
    def __init__(self, predicate, true_exp, else_exp, *args, **kwargs):
        super(IfElse, self).__init__(short_name='i', long_name='IfElse', desc='IfElse',
                                    *args, **kwargs)
        self.predicate = predicate
        self.true_exp = true_exp
        self.false_exp = else_exp

    def evaluate(self, table):
        predicate = self.predicate
        true_exp = self.true_exp
        false_exp = self.false_exp

        if not isinstance(table, pd.Panel) and \
                not isinstance(table, pd.DataFrame) and \
                not isinstance(table, pd.Series):
            raise RuntimeError("Pandas's Panel/DataFrame/Series is needed for table!")

        if not predicate or not true_exp or not false_exp:
            raise RuntimeError("predicate, true_exp and else_exp has to be assigned and not None")

        pred_val = predicate.evaluate(table)
        true_val = true_exp.evaluate(table)
        false_val = false_exp.evaluate(table)

        # out_val = ifelse_fn(pred_val.values, true_val.values, false_val.values)

        pred_arr = None
        if isinstance(pred_val, pd.Panel) or isinstance(pred_val, pd.DataFrame) or isinstance(pred_val, pd.Series):
            pred_arr = pred_val.values
        else:
            pred_arr = pred_val

        out_val = np.zeros(pred_arr.shape)
        out_val[pred_arr] = true_val
        out_val[np.logical_not(pred_arr)] = false_val
        return pd.DataFrame(data=out_val, index=pred_val.index)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + "," + repr(self.periods) + ")"

