# Knight Probability in Chessboard -> Python3

'''
Explanation: Start with probability 1 and on every step the weight added to probability is the 
previous value divided by 8 given all 8 possible moves. In case of move landing outside board the 
probability is 0 and if inside board then recursive dfs call to get probability of remaining steps 
within limit.
'''

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        mem, mov = {}, ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        def dfs(a, b, p, q):
            if 0 <= a < n and 0 <= b < n and q < k:
                sm = 0
                for x, y in mov:
                    if (a + x, b + y, q) not in mem:
                        mem[(a + x, b + y, q)] = dfs(a + x, b + y, p / 8, q + 1)
                    sm += mem[(a + x, b + y, q)]
                return sm
            else: return 0 <= a < n and 0 <= b < n and p or 0
        return dfs(row, column, 1, 0)