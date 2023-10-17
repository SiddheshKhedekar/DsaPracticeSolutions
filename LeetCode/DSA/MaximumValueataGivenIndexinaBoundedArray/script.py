# Maximum Value at a Given Index in a Bounded Array -> Python3

'''
Explanation: Decrement maxSum by n  then set l, r as 0, maxSum wun binary search on l, r set m  and 
check if func at m is less than maxsum to set l as m else set r as m and return l. Inside func set 
y as max of x - index, 0 and ans as (x + y) * (x - y + 1) floor div by 2. Set y again as the max of 
x - ((n - 1)-index), 0 and increment ans by the original set value then return ans - x.
'''

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def func(x):
            y = max(x - index, 0)
            ans = (x + y) * (x - y + 1) // 2
            y = max(x - ((n - 1) - index), 0)
            ans += (x + y) * (x - y + 1) // 2
            return ans - x
        maxSum -= n
        l, r = 0, maxSum
        while l < r:
            m = (l + r + 1) // 2
            if func(m) <= maxSum: l = m
            else: r = m - 1
        return l + 1