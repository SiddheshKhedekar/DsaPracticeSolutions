# Rearrange Array Elements by Sign -> Python3

'''
Explanation: Assign pos, neg to 0 and create ans as array of 0 with size len nums. Then loop on 
each item x in nums and check if x is positive to assign ans at pos as x and increment pos by 2 
then in else do the same for neg and finally return the ans.
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans, pos, neg = [0] * len(nums), 0, 1
        for x in nums:
            if x > 0: ans[pos], pos = x, pos + 2
            else: ans[neg], neg = x, neg + 2
        return ans