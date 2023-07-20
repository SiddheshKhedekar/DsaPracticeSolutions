# Maximum Number of Events That Can Be Attended II -> Python3

'''
Explanation: Sort the events by the second item in arrayitem and initialize dp1 and dp2 as array of 
arrayitem 0,0. Loop on k times and inside set s, e, v by iterating events then set x as bisect on 
dp1, s as array and after subtracting 1. Check if dp1 value at x, 1 after adding v is greater than 
dp2 value at -1,1 and append the array item of e, sp1 at x, 1 after adding v to dp2 then in outer 
loop aet dp1 as dp2 and dp2 as it was at init. Finally return the dp1 at -1,-1.
'''

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda sev: sev[1])
        dp1, dp2 = [[0, 0]], [[0, 0]]
        for _ in range(k):
            for s, e, v in events:
                x = bisect.bisect(dp1, [s]) - 1
                if dp1[x][1] + v > dp2[-1][1]:
                    dp2.append([e, dp1[x][1] + v])
            dp1, dp2 = dp2, [[0, 0]]
        return dp1[-1][-1]