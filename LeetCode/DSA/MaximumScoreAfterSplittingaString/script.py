# Maximum Score After Splitting a String -> Python3

'''
Explanation: Set zeroes and score as 0 and ones as count of 1 in s then loop till the last index in 
s to check if 1 found at current index and decrement ones or 0 found and increment zeroes. Set the 
score as max of itself and sum of zeroes and ones. Finally return score at end of loop.
'''

class Solution:
    def maxScore(self, s: str) -> int:
        score, zeroes, ones = 0, 0, s.count('1')
        for x in range(len(s) - 1):
            zeroes += s[x] == '0'
            ones -= s[x] == '1'
            score = max(zeroes + ones, score)
        return score