# Maximal Square -> Python3

'''
Explanation: Maintain grid of dp and iterate over rows then cos of input. Inside check if 
corresponding nodes are 1 to set next dp and max node. At end return max node multiplied by itself.
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1: return 0
        rows, cols, mx = len(matrix), len(matrix[0]), 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    dp[row + 1][col + 1] = min(dp[row][col],dp[row + 1][col],dp[row][col + 1]) + 1
                    mx = max(mx, dp[row + 1][col + 1])
        return mx * mx