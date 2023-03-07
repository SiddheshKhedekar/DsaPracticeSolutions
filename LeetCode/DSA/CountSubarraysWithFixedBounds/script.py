# Count Subarrays With Fixed Bounds -> Python3

'''
Explanation: Maintain ans as 0 and three pointers min, max and fail to -1. Iterate on the 
enumerated nums and set fail to index if not in constraint. Set min, max to index if value is as 
set in input and increment ans by the max of 0 and min of (min, max) - fail.
'''

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans, mn, mx, fl = 0, -1, -1, -1
        for indx, num in enumerate(nums):
            if not minK <= num <= maxK: fl = indx
            if num == minK: mn = indx
            if num == maxK: mx = indx
            ans += max(0, min(mn, mx) - fl)
        return ans