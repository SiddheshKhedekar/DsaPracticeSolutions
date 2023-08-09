# Find the Smallest Divisor Given a Threshold -> Python3

'''
Explanation: Run binary search from 1 to max of nums and in if check with mid for condition to set 
r as mid else left is mid. In check function we need to return the sum of all n -1 floor divide by 
divisor pased for all n in nums and check if it is less than or same as threshold.
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(d): return sum((n - 1) // d + 1 for n in nums) <= threshold
        l, r = 1, max(nums)
        while l < r:
            m = l + (r - l) // 2
            if check(m): r = m
            else: l = m + 1
        return l