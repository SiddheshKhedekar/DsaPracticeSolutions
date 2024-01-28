# Reshape Data: Pivot -> Python3

'''
Explanation: The pivot function can transform data using index columns and values params by passing 
original column headers as needed. 
'''

import pandas as pd
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index = 'month', columns = 'city', values = 'temperature')