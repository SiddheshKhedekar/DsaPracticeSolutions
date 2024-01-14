# Create a DataFrame from List -> Python3

'''
Explanation: Use the dataframe method to return the columns requested from studentdata.
'''

import pandas as pd
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id', 'age'])