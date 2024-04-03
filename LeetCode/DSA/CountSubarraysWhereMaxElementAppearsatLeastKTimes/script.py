# Count Subarrays Where Max Element Appears at Least K Times -> Python3

'''
Explanation: Set mx as max of nums and ans, crnt, x as 0. Then use a sliding window to keep a 
maximum subarray nums x to y with at most k - 1 times of a. For all subarrays starting before nums 
at x and ending at y, we will have at least k times of mx. So we increment ans by x and return ans 
at end of loop.
'''

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx, ans, crnt, x = max(nums), 0, 0, 0
        for y in range(len(nums)):
            crnt += nums[y] == mx
            while crnt >= k:
                crnt -= nums[x] == mx
                x += 1
            ans += x
        return ans