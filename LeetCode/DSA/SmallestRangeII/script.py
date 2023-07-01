# Smallest Range II -> Python3

'''
Explanation: First sort the numbers and then starting from the smallest we add 2 * k to the values 
in  nums hoping it reduces the difference of max and min, return the min of x + 2 * k - y after 
calculating the values from gap and gap from 1.
'''

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        mx, mn = max(nums), min(nums)
        if mx - mn >= 4 * k: return mx - mn - 2 * k
        if mx - mn <= k: return mx - mn
        gap = sorted([x for x in nums if mx - 2 * k < x < mn + 2 * k] + \
                [mx - 2 * k, mn + 2 * k])
        return min(x + 2 * k - y for x, y in zip(gap, gap[1:]))