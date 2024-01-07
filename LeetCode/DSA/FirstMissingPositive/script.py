# First Missing Positive -> Python3

'''
Explanation: First loop to delete the useless elements by checking for length and if values in 
range else set 0. Run another loop and increment l to nums at (nums x) mod by l. Run another loop 
from 1 to len and check if the floor division of nums at x by l and check if 0 to return x 
otherwise return l at end. 
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        l = len(nums)
        for x in range(len(nums)):
            if nums[x] < 0 or nums[x] >= l: nums[x] = 0
        for x in range(len(nums)): nums[nums[x] % l] += l
        for x in range(1, len(nums)):
            if nums[x] // l == 0: return x
        return l