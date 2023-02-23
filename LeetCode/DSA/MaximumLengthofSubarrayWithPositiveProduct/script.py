# Maximum Length of Subarray With Positive Product -> Python3

'''
Explanation: Set pos and neg arrays and ans to pos[0] then loop on range len nums from 1. If 
nums[cur] is greater than 0 then set pos[cur] to 1 plus pos[prev] and neg[cur] similar to pos based 
on neg[prev] value elseif nums[cur] less than 0 then do the reverse. Finally set ans to max of ans 
and pos[cur].
'''

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = [0] * n, [0] * n
        if nums[0] > 0: pos[0] = 1
        if nums[0] < 0: neg[0] = 1
        ans = pos[0]
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            ans = max(ans, pos[i])
        return ans