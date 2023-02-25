# Partition Labels -> Python3

'''
Explanation: Save the rightmost indices of chars. Set the right pointer to the max of right and 
rightmost. When the index and right pointer are the same reset the left pointer and add the 
difference between pointers to the result.
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rm = {k:v for v, k in enumerate(s)}
        l, r, res = 0, 0, []
        for ind, char in enumerate(s):
            r = max(r, rm[char])
            if ind == r:
                res += [r - l + 1]
                l = ind + 1
        return res