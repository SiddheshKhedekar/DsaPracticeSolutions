# Method Chaining -> Python3

'''
Explanation: Return the dataset by filtering on condition of weight and then sort values by it.
'''

import pandas as pd
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(['weight'], ascending = False)[['name']]