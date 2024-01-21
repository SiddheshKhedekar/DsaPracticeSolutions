# Drop Missing Data -> Python3

'''
Explanation: Return the dataset by checking if the column name is notnull using inbuild function.
'''

import pandas as pd
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['name'].notnull()]