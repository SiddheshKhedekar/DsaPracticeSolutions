# Koko Eating Bananas -> Python3

'''
Explanation: Set start, end then loop while start is less than end. Set middle and check if not 
func mid and set start as mid else set end as mid. Return start on loop end and define func as 
returning if the sum of pil - 1 floor divide by i for pil in piles is less than or same as h.
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        def func(i): return sum((pil - 1) // i + 1 for pil in piles) <= h
        while start < end:
            middle = (start + end) // 2
            if not func(middle): start = middle + 1
            else: end = middle
        return start