# Reducing Dishes -> Python3

'''
Explanation: Initialize ans, tot as 0 and sort input. Run loop while input and last item of 
input + tot is greater than 0. Increment tot by pop on input and increment ans by tot.
'''

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = tot = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + tot > 0:
            tot += satisfaction.pop()
            ans += tot
        return ans