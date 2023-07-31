# Longest Arithmetic Subsequence -> Python3

'''
Explanation: We know dp at index,diff is same as the length of arithmetic sequence at index with 
difference diff. So we run nested loops for x and y then set dp at y , diff between nums at y and x 
as the dp by get on x, diff between nums at y and x, 1 after adding 1. Finally we return the max of 
values in dp.
'''

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                dp[y, nums[y] - nums[x]] = dp.get((x, nums[y] - nums[x]), 1) + 1
        return max(dp.values())