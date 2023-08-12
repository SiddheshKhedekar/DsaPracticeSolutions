# H-Index II -> Python3

'''
Explanation: Check if citations not received, then return 0. Set the len of citations and low, high 
of indexes then run loop while low is less than or same as high. Inside loop set mid as floor 
division of low and high sum then check if m + citations at m is greater than l to set high as m - 
1 else low will be m + 1 and finally return l - low.
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        l = len(citations)
        low, high = 0, l - 1
        while low <= high:
            m = (low + high) // 2
            if m + citations[m] >= l: high = m - 1
            else: low = m + 1
        return l - low