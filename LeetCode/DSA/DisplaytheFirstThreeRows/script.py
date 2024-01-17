# Display the First Three Rows -> Python3

'''
Explanation: The head function can be used on dataframe to return the first n number of rows.
'''

import pandas as pd
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame: return employees.head(3)