# Largest Substring Between Two Equal Characters -> Python3

'''
Explanation: Store the first index of the substring between same characters then if current ch seen 
before, compute the length of the subtring between them and update the max length.
'''

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mxl, indices = -1, {}
        for x, ch in enumerate(s): mxl = max(mxl, x - indices.setdefault(ch, x + 1)); print(indices)
        return mxl