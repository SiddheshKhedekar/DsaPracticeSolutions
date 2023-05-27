# Partition Equal Subset Sum -> Python3

'''
Explanation: Set tot as the sum of nums and check if tot & 1 to return false then set hlf, dp as 
tot floor divide by 2, 1. Run for loop to set dp |= dp << n and at end return the dp & 1 << hlf.
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot & 1: return False
        hlf, dp = tot // 2, 1
        for n in nums: dp |= dp << n
        return dp & 1 << hlf