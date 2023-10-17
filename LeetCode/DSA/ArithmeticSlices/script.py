# Arithmetic Slices -> Python3

'''
Explanation: Set l, dp, dpPrev, res as len nums, 0, 0, 0 and run loop for range 2 to l. Check if 
numx subtraction of x-1 and x-2 is same as x and x-1 to set dp as dpPrev + 1. Increment res by dp, 
set dp prev as dp and dp as 0.
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l, dp, dpPrev, res = len(nums), 0, 0, 0
        for x in range(2, l):
            if nums[x - 1] - nums[x - 2] == nums[x] - nums[x - 1]:
                dp = dpPrev + 1
            res += dp
            dpPrev, dp = dp, 0
        return res