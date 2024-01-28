# Reshape Data: Melt -> Python3

'''
Explanation: The melt function can transform data using id_vars set to product as array, var_name 
as quarter and value_name as sales.
'''

import pandas as pd
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars = ['product'], var_name = 'quarter', value_name = 'sales')