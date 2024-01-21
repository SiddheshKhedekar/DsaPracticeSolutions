# Modify Columns -> Python3

'''
Explanation: The assign function can be used to set the salary to its twice in the dataset.
'''

import pandas as pd
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary = 2 * employees['salary'])