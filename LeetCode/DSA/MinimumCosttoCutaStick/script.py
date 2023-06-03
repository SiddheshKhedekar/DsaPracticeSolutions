# Minimum Cost to Cut a Stick -> Python3

'''
Explanation: Redefine cuts as sorted cuts along with addition of 0 and n, then get len of cuts in l 
and set dp as grid of [0] l by l. Run loop on range 2 to l and inside run loop 0 to l - x to set dp 
at y, y + x as the min of dp at y,z + dp att z, y + x for all z in range y + 1  to y + x after 
adding cuts at y + x and subtracting cuts at y and finally return dp at 0, l-1.
'''

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts + [0, n])
        l = len(cuts)
        dp = [[0] * l for _ in range(l)]
        for x in range(2, l):
            for y in range(l - x):
                dp[y][y + x] = min(dp[y][z] + dp[z][y + x] \
                for z in range(y + 1, y + x)) + cuts[y + x] - cuts[y]
        return dp[0][l - 1]