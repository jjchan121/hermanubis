
from unittest import TestCase
# from hermanubis.expression import Expression
# from hermanubis.arithmetic_operator import Plus
import pandas as pd
import numpy as np
from hermanubis.column import Column
from hermanubis.expressions import Plus
from hermanubis.cross_section import Abs, Average
from hermanubis.delta import Delta, Delay
from hermanubis.functions import FuncWrapper






close = Column('Close')
log_close = FuncWrapper(close, func=np.log, long_name='Log', short_name='l', desc='Logarithm')
log_ret = Delta(log_close, periods=1, fillna_val=0)
avg = Average(log_ret)
cross_section_ret = log_ret - Average(log_ret)
weight = cross_section_ret / Abs(cross_section_ret)

pf = pd.read_pickle('/Volumes/Transcend/data/HSI_const.pkl')


log_close.evaluate(pf)
log_ret0 = log_ret.evaluate(pf)
avg_ret0 = avg.evaluate(pf)
cross0 = cross_section_ret.evaluate(pf)


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

minus_on_unequal_shape(log_ret0, avg_ret0)
minus_on_unequal_shape(avg_ret0, log_ret0)

avg_ret0.shape

log_ret0.shape[1]

np.transpose(np.vstack([test_arr for i in range(5)]))

pf.loc[:, '2000-01-04', :]

close0 = pf.loc[:, :, 'Close']
volume = pf.loc[:, :, 'Volume']

slice = pf.major_xs('2017-06-16')

slice.loc[:, :, 'Close']


close.rolling(np.sum, axis=0, window=4)

close.rolling_sum(window=4)

df = pf.loc[:,'2017-06-16',:]



df = pf.loc[:, :, 'Close']
rank = df.rank(axis=1)/(df.shape[1]-1)


open = Column('Open')
close = Column('Close')

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(searchpath='templates/')
)

tmp = env.get_template('single_var_rolling.html')
print (tmp.render({"className" : 'Sum'}))


nested_list = ['+', ['*', ['-', 'a', 'b'], ['>', 'c','d']], ['a']]
import itertools
l1_f = itertools.chain(*nested_list)

# print a nested list
# use itertools.chain(*nested_list)
# use next to iterate, if not nested, put into array, if nested, put into another list

df = pd.DataFrame({"A" : np.linspace(0,1,20), "B": np.linspace(-2,-1,20)})

a = Column('A')
b = Column('B')

c = Abs(b)


c = a + b
c.evaluate(df)