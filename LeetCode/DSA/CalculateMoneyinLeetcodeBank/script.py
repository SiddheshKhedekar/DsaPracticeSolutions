# Calculate Money in Leetcode Bank -> Python3

'''
Explanation: The problem is the form of a arithmetic progression and as such for a week the sum is 
28 and each next week it will increase by 7 multiplied by the week number from start 0. For the 
rest of the days we need to calculate using loop and incrementing the values accordingly.
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7: return n * (n + 1) // 2
        wks = n // 7
        res = wks * 28
        res += (wks * (wks - 1) * 7) // 2
        if n % 7 != 0:
            ds, d = n % 7, wks + 1
            for j in range(ds):
                res += d
                d += 1
        return res