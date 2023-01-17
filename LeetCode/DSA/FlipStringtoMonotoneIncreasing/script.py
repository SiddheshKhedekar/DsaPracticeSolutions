# Flip String to Monotone Increasing -> Python3

'''
Explanation: Get length of string and count of 0 and initially set count of 1 as 0 along with final 
count as count of 1. Then run a for loop on length and decrement count of 0 when encountered else 
set the final count to min of it and sum of both counters and increment count of 1.
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        l, count0, count1 = len(s), s.count('0'), 0
        ans = l - count0
        for x in range(l):
            if s[x] == '0': count0 -= 1
            else:
                ans = min(ans, count1+count0)
                count1 += 1
        return ans