# Max Consecutive Ones III -> Python3

'''
Explanation: Implementing sliding window using x as 0 and looping on y in range len nums. Decrement 
k by 1 - nums at y then check if k is less than 0 to increment k by 1 - nums at x and x by 1. At 
end of loop return y - x + 1.
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        x = 0
        for y in range(len(nums)):
            k -= 1 - nums[y]
            if k < 0:
                k += 1 - nums[x]
                x += 1
        return y - x + 1