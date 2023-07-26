# Minimum Speed to Arrive on Time -> Python3

'''
Explanation: Implement binary search by setting low, high, l as 1, max value, len of distance then 
loop while low is less than high. Inside set speed as the mid of low and high and need as the last 
element in dis divided by speed and add the sum of all dist values at x  plus speed - 1 floor 
divide by speed for all x in range l-1. Then check if need is greater than hour to set low as speed 
else high is speed. Finally return -1 if low is max value else low.
'''

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low, high, l = 1, 10 ** 7 + 1, len(dist)
        while low < high:
            speed = low + (high - low) // 2
            need = dist[-1] / speed + sum((dist[x] + speed - 1) // speed for x in range(l - 1))
            if need > hour: low = speed + 1
            else: high = speed
        return -1 if low == 10 ** 7 + 1 else low