# Minimum Time to Complete Trips -> Python3

'''
Explanation: Set start, end then loop while start is less than end. Set middle and check if not 
func mid and set start as mid else set end as mid. Return start on loop end and define func as 
returning if the sum of i divide by tim in time is greater than or same as totaltrips.
'''

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start, end = 1, totalTrips * min(time)
        def func(i): return sum(i // tim for tim in time) >= totalTrips
        while start < end:
            middle = (start + end) // 2
            if not func(middle): start = middle + 1
            else: end = middle
        return start