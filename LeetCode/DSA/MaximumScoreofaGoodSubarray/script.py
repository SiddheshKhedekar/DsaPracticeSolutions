# Maximum Score of a Good Subarray -> Python3

'''
Explanation: Initialize ans,mn as nums at k, also set x, y as k and l as len of nums. Then run loop 
while x is greater than 0 or y is less than l - 1, inside check if nums at x - 1 is less than nums 
at y + 1 if x, y is valid else 0 to increment y by 1 else decrement x by 1. Set mn as min of mn, 
nums at x and y then set ans as the max of ans, mn multiplied by y - x + 1. Finally, return ans.
'''

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = mn = nums[k]
        x, y, l = k, k, len(nums)
        while x > 0 or y < l - 1:
            if (nums[x - 1] if x else 0) < (nums[y + 1] if y < l - 1 else 0): y += 1
            else: x -= 1
            mn = min(mn, nums[x], nums[y])
            ans = max(ans, mn * (y - x + 1))
        return ans