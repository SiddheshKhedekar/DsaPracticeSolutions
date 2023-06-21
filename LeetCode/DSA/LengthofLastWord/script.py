# Length of Last Word -> Python3

'''
Explanation: Set end to len-1, run while loop till end > 0 and s[end] = ' ' inside decrement end by 
1, set beg to end then run loop till beg >= 0 and s[beg] != ' ' inside decrement beg by 1 finally 
return end-beg.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s)-1
        while end > 0 and s[end] == ' ': end-=1
        beg = end
        while beg >= 0 and s[beg] != ' ': beg-=1
        return end - beg