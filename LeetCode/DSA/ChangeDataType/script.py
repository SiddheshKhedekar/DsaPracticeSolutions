# Change Data Type -> Python3

'''
Explanation: The assign function updates value of dataframe column and astype can cast to int.
'''

import pandas as pd
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.assign(grade = students['grade'].astype(int))