# Minimum Length of String After Deleting Similar Ends -> Python3

'''
Explanation: Run loop while len of s is greater than 1 and the value at front and end is the same 
to set s as its value after stripping the value of s at 0 then outside loop return len s.
'''

class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]: s = s.strip(s[0])
        return len(s)