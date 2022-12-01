# Determine if String Halves Are Alike -> Python3

'''
Explanation: Use a set of defined vowels and count the vowvels in each half.
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow, first, second, x, y = set('aeiouAEIOU'), 0, 0, 0, len(s) - 1
        while x < y:
            first += s[x] in vow 
            second += s[y] in vow
            x, y = x+1, y-1
        return first == second