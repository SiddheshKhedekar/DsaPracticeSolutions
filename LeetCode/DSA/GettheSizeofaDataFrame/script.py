# Get the Size of a DataFrame -> Python3

'''
Explanation: The shape method can be used on dataframe to return list of values needed.
'''

import pandas as pd
def getDataframeSize(players: pd.DataFrame) -> List[int]: return list(players.shape)