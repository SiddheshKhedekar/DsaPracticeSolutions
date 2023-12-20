# Maximum Product Difference Between Two Pairs -> Python3

'''
Explanation: Set mn1, mn2 as max and mx1, mx2 as least possible values then loop on num in nums. 
Set mn1, mn2 by comparing to num in if and elif then similarly set mx1, mx2. Lastly return the 
product of mx - mn.
'''

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mn1 = mn2 = float('inf')
        mx1 = mx2 = float('-inf')
        for num in nums:
            if num <= mn1: mn1, mn2 = num, mn1
            elif num < mn2: mn2 = num
            if num >= mx1: mx1, mx2 = num, mx1
            elif num > mx2: mx2 = num
        return mx1 * mx2 - mn1 * mn2