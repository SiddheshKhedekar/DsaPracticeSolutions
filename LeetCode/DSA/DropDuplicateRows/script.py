# Drop Duplicate Rows -> Python3

'''
Explanation: Use the drop duplicates function on datased to delete based on subset email.
'''

import pandas as pd
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = ['email'])