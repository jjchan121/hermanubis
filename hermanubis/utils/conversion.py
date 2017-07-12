import raccoon as rc
import pandas as pd
import numpy as np
import datetime


def rc_to_pd(raccoon_dataframe):
    """
    Convert a raccoon dataframe to pandas dataframe

    :param raccoon_dataframe: raccoon DataFrame
    :return: pandas DataFrame
    """
    data_dict = raccoon_dataframe.to_dict(index=False)
    return pd.DataFrame(data_dict, columns=raccoon_dataframe.columns, index=raccoon_dataframe.index)


def pd_to_rc(pandas_dataframe):
    """
    Convert a pandas dataframe to raccoon dataframe

    :param pandas_dataframe: pandas DataFrame
    :return: raccoon DataFrame
    """

    columns = pandas_dataframe.columns.tolist()
    data = dict()
    pandas_data = pandas_dataframe.values.T.tolist()
    for i in range(len(columns)):
        data[columns[i]] = pandas_data[i]
    index = pandas_dataframe.index.tolist()
    index_name = pandas_dataframe.index.name
    index_name = 'index' if not index_name else index_name
    return rc.DataFrame(data=data, columns=columns, index=index, index_name=index_name)



def rc_to_mindex_pd(raccoon_dataframe: rc.DataFrame, col_4_indexs: list):
    """
    Convert a raccoon dataframe to pandas MultiIndex dataframe

    :param raccoon_dataframe: raccoon DataFrame
    :return: pandas DataFrame
    """

    multi_index = pd.MultiIndex.from_arrays(raccoon_dataframe[col_4_indexs].data)



    data_dict = raccoon_dataframe.to_dict(index=False)
    return pd.DataFrame(data_dict, columns=raccoon_dataframe.columns, index=multi_index)

#
# num_sym = 1000
# N = 60*6*num_sym
#
# symbols = [("%s.HK" % str(i+1)) for i in np.random.choice(num_sym, N)]
#
# now = datetime.datetime.now()
#
# import itertools
# ts_list = [[now + datetime.timedelta(minutes=i) for i in range(360)] for j in range(num_sym)]
# timestamps = list(itertools.chain(*ts_list))
#
# sym_list = [["%s.HK" % str(j+1) for i in range(360)] for j in range(num_sym)]
# symbols = list(itertools.chain(*sym_list))
#
# rdf = rc.DataFrame({
#     "DateTime" : timestamps,
#     "Open" : np.random.normal(100,1,N).tolist(),
#     "High" : np.random.normal(100,1,N).tolist(),
#     "Low" : np.random.normal(100,1,N).tolist(),
#     "Close" : np.random.normal(100,1,N).tolist(),
#     "Symbol" : symbols
# })
#
# import sys
# sys.getsizeof(rdf)
#
# %time df = rc_to_pd(rdf)
#
#
#
# # %timeit midf = rc_to_mindex_pd(rdf, ['DateTime', 'Symbol'])
# midf = rc_to_mindex_pd(rdf, ['DateTime', 'Symbol'])
#
# pf = midf.to_panel()
#
# %timeit
# midf.xs('Close', axis=1).unstack()
# %timeit pf.loc['Close',:,:]
#
# midf['Close']

"""
for later Pandas it is recommended to use multiindex dataframe instead of Panel
"""
# pd.MultiIndex.from_array(rdf[['Date', 'Symbol']].data)

# dfmi.xs('Close', axis=1).unstack()

#check if it is multiindex dataframe
# if isinstance(result.index, pandas.core.index.MultiIndex):


