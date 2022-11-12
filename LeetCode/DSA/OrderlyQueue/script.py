# Orderly Queue -> Python3

'''
Explanation: If k > 1 return sorted s else loop for i in range len s and get the min of s[i:]+s[:i].
'''

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return ''.join(sorted(s)) if k > 1 else min(s[i:]+s[:i] for i in range(len(s)))