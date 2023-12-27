# Largest Rectangle in Histogram -> Python3

'''
Explanation: Add 0 in heights and set stk to -1 in array format along with res to 0. Loop for x in 
range len heights and loop again while heights at x is less than it at last index of stk. Inside 
set hgt wdt as heights at stk pop and x - stk at last index - 1 then set res as max of res, new 
area of hgt wdt. Outside while loop append x in stk and outside for pop heights then return res.
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stk, res = [-1], 0
        for x in range(len(heights)):
            while heights[x] < heights[stk[-1]]:
                hgt, wdt = heights[stk.pop()], x - stk[-1] - 1
                res = max(res, hgt * wdt)
            stk.append(x)
        heights.pop()
        return res