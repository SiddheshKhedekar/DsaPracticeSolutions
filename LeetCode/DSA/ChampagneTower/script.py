# Champagne Tower -> Python3

'''
Explanation: Initialize ans as array of poured + 0 array of size query_row. Then loop on r in range 
1 to query_row and loop again for range from r to 1 in reverse. Inside set ans at x as max of ans 
at x - 1, 0 divided by 2 after adding the max of ans at [x - 1] -1, 0 divided by 2. At end return 
the min of ans at query_glass, 1.
'''

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        ans = [poured] + [0] * query_row
        for r in range(1, query_row + 1):
            for x in range(r, -1, -1):
                ans[x] = max(ans[x] - 1, 0) / 2.0 + max(ans[x - 1] - 1, 0) / 2.0
        return min(ans[query_glass], 1)