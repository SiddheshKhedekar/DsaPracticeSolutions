# Reshape Data: Concatenate -> Python3

'''
Explanation: The concat function can merge two dataframes passed to it as array items.
'''

import pandas as pd
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame): return pd.concat([df1, df2])