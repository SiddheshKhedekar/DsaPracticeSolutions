# Create a New Column -> Python3

'''
Explanation: The assign function can add column to dataframe and set its value as requested.
'''

import pandas as pd
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus = 2 * employees['salary'])