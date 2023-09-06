# Permutation in String -> Python3

'''
Explanation: Set frequency and increment and decrement in cases finally check match = len counter 
and return true otherwise it is false set w as len s1. Run for loop in range len s2 and if s2 i in 
cntr then check if not cntr[s2[i]] decrement match by 1 first decrement cntr same by 1 and 
increment for same above cntr condition by 1. In second if check i >= w and s2[i-w] in cntr do same 
if subcondition for i-w and just increment cntr by 1.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, match = Counter(s1), len(s1), 0
        for i in range(len(s2)):
            if s2[i] in cntr:
                if not cntr[s2[i]]: match -= 1
                cntr[s2[i]] -= 1
                if not cntr[s2[i]] : match += 1
            if i >= w and s2[i-w] in cntr:
                if not cntr[s2[i-w]]: match -= 1
                cntr[s2[i-w]] += 1
                if not cntr[s2[i-w]] : match += 1
            if match == len(cntr): return True
        return False