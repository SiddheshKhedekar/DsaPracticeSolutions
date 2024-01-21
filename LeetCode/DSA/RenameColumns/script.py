# Rename Columns -> Python3

'''
Explanation: Assign new column names using the rename function for the dataset.
'''

import pandas as pd
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id":"student_id","first":"first_name",
        "last":"last_name","age":"age_in_years"})