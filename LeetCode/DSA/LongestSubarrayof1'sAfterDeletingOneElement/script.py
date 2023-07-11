# Longest Subarray of 1's After Deleting One Element -> Python3

'''
Explanation: Set z as 1 and x as 0 then loop on y in range of len nums. Inside decrement z by nums 
y == 0 then check if z is less than 0 and increment z by nums x == 0 and x by 1 and at end return 
y - x.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        z, x = 1, 0
        for y in range(len(nums)):
            z -= nums[y] == 0
            if z < 0:
                z += nums[x] == 0
                x += 1
        return y - x