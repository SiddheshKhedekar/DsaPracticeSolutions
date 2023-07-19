# Tallest Billboard -> Python3

'''
Explanation: We set dp at any index v as the max of pair of sum we get with pair difference v. For 
case where we put i to the tall side we update dp at v + i as the max of dp value at d + x, y. For 
case where we put i to the short side we update dp at abs v - i as the max of dp at abs v - i, 0 and 
j + min of v, i. We have final return value at 0 in dp.
'''

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for i in rods:
            for v, j in dp.copy().items():
                dp[v + i] = max(dp.get(i + v, 0), j)
                dp[abs(v - i)] = max(dp.get(abs(v - i), 0), j + min(v, i))
        return dp[0]