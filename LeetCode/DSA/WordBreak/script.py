# Word Break -> Python3

'''
Explanation: Set res as array of single true then run loop for range 1 to len s + 1. Inside 
increment res as any res at y and sfrom y to s in worddict for all y in range x by using, operation 
and on loop end return last res as res indicates if the  strings upto i can be made.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True]
        for x in range(1, len(s) + 1):
            res += any(res[y] and s[y:x] in wordDict for y in range(x)),
        return res[-1]