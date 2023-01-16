# Minimum Size Subarray Sum -> Python3

'''
Explanation: Use two pointers and run a for loop on the second. Subtract y value from target and 
run loop on target get min ans update target and increment x. Return ans mod by length. 
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        x, ans = 0, len(nums) + 1
        for y in range(len(nums)):
            target -= nums[y]
            while target <= 0:
                ans = min(ans, y - x + 1)
                target += nums[x]
                x += 1
        return ans % (len(nums) + 1)