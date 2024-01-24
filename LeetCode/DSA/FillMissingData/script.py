# Fill Missing Data -> Python3

'''
Explanation: The fillna function will replace column null entries with assigned value.
'''

import pandas as pd
def fillMissingValues(products: pd.DataFrame): return products.fillna(value = {'quantity' : 0})