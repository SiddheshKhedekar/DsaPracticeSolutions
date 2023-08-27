# Delete Operation for Two Strings -> Python3

'''
Explanation: Check if len of word1 is less than word2 and swap words then set dp as array of 2 rows 
with column of length word2 + 1 where each array item is 1000. Run nested for loop on range og len 
word1+1 and then inside word2+1. Then set dp at x & 1, y as x + y if x is 0 or y is 0 else set it 
as its dp value for previous x and y only if word1 at x-1 is same as word2 at y -1 else set it as 
1 + min of dp at prev x, y or x, prev y. Finally return the dp at len word1 & 1, -1.
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2): word1, word2 = word2, word1
        dp = [[1000] * (len(word2) + 1) for _ in range(2)]
        for x in range(len(word1) + 1):
            for y in range(len(word2) + 1):
                dp[x & 1][y] = x + y if x == 0 or y == 0 else dp[(x - 1) & 1][y - 1] \
                if word1[x - 1] == word2[y - 1] else 1 + min(dp[(x - 1) & 1][y], dp[x & 1][y - 1])
        return dp[len(word1) & 1][-1]