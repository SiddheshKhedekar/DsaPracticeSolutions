# House Robber II -> Python3

'''
Explanation: Rob house twice by implementing a helper function. First on index 0 and remaining list 
from index 2 to -1. And second time from index 1 to end and then return the max of both.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            last, now = 0, 0
            for num in nums: last , now = now, max(last+num, now)
            return now
        return max(nums[0] + rob_helper(nums[2:-1]),rob_helper(nums[1:]))