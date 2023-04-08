# Scramble String -> Python3

'''
Explanation: Initialize x, y as len of s1, s2 and func as call to function. If lengths don't match 
or sorted strings are not equal then return false. If s1 len is less than 4 or s1 equal to s2 then 
return true. Then loop on range 1 to len of s1 and check if func call of s1 and s2 up to z and that 
from z to end or func call where s1 same as before but s2 call -z to end and start to -z then 
return true else at end of func return false.
'''

class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        x, y, func = len(s1), len(s2), self.isScramble
        if x != y or sorted(s1) != sorted(s2): return False
        if x < 4 or s1 == s2: return True
        for z in range(1, x):
            if func(s1[:z], s2[:z]) and func(s1[z:], s2[z:]) or \
                func(s1[:z], s2[-z:]) and func(s1[z:], s2[:-z]): return True
        return False