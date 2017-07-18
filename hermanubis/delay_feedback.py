import pandas as pd
import numpy as np
# import theano
# import theano.tensor as tt
from hermanubis.expressions import Expression


# theano.config.compute_test_value = 'off'
#
# alpha = tt.fmatrix('alpha')
# w = tt.fscalar('w')
# a0 = tt.fvector()
#
# def accumulate_with_delay(a, prev_a):
#     return a + prev_a
#     # return prev_a *w + a * (1-w)
#
#
# out, update = theano.scan(fn=accumulate_with_delay,
#                           # sequences=dict(input=alpha, taps=[-1, -0]),
#                           sequences=alpha,
#                           # outputs_info=[dict(initial=alpha[0,:], taps=[-1,-0]), a0],
#                           # outputs_info=alpha[0,:],
#                           # outputs_info=alpha[0,:],
#                           outputs_info=tt.zeros_like(alpha[0,:]),)
#                           # non_sequences=[w],)
#
#
# accum_fn = theano.function(inputs=[alpha],
#                            outputs=out,
#                            # updates=update,
#                            allow_input_downcast=True)
#
#
# alpha0 = np.array([[0.1, 0.2, 0.3], [0.7, 0.8, 0.9], [1.0, 2, 3], [5,6,7]])
# accum_fn(alpha0, 1.0)
# accum_fn(alpha0)

def np_accum_with_w_1d(alpha, w):
    out_arr = np.zeros_like(alpha)
    out_arr[0] = alpha[0]
    for i in range(1, alpha.shape[0]):
        out_arr[i] = w * alpha[i] + (1 - w) * out_arr[i - 1]

    return out_arr


def np_accum_with_w_2d(alpha, w):
    out_arr = np.zeros_like(alpha)
    out_arr[0, :] = alpha[0, :]
    for i in range(1, alpha.shape[0]):
        out_arr[i,:] = w * alpha[i, :] + (1 - w) * out_arr[i - 1, :]

    return out_arr


class DelayFeedback(Expression):
    def __init__(self, expr, weight, long_name, *args, **kwargs):
        super(DelayFeedback, self).__init__(short_name='D', long_name=long_name, desc='DelayFeedback', *args, **kwargs)
        self.expr = expr
        self.weight = weight

    def evaluate(self, table):
        expr = self.expr
        val = expr.evaluate(table)
        if isinstance(val, pd.Panel):
            raise RuntimeError("Panel is not supported in DelayFeedback")

        out_arr = np_accum_with_w_2d(val.values, self.weight)
        return pd.DataFrame(out_arr, index=val.index, columns=[self.long_name])

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.long_name + "(" + repr(self.expr) + ")"


