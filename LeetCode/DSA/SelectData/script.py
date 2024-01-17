# Select Data -> Python3

'''
Explanation: We can return the student by checking for id and fetch the columns needed.
'''

import pandas as pd
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]