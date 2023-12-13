# Maximum Product of Two Elements in an Array -> Python3

'''
Explanation: Set mx1, mx2 to least number possible then loop on n in nums check if n is greater 
than mx1 to set mx2 as mx1 and mx1 as n also check for n greater than mx2 and set mx2 as n finally 
return the product requested.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = -math.inf
        for no in nums:
            if no > m1: m2, m1 = m1, no
            elif no > m2: m2 = no
        return (m1 - 1) * (m2 - 1)