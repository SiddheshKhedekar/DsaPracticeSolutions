# Minimum Number of Steps to Make Two Strings Anagram -> Python3

'''
Explanation: Get the count of all chars in string s and t as c1, c2 then subtract c2 from c1 and 
return the sum of its values.
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = map(Counter, (s, t))
        return sum((c1 - c2).values())