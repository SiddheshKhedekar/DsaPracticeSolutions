# Greatest Common Divisor of Strings -> Python3

'''
Explanation: Check if inputs are valid and return valid one. Else check for length and return 
recursive call with greater length string as first input. Else check if the greater string up to 
length of smaller one and the other string are equal and retutn the checked strings in recursive 
call and if no contition matches then return empty string.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2: return str1 if str1 else str2
        elif len(str1) < len(str2): return self.gcdOfStrings(str2, str1)
        elif str1[:len(str2)] == str2: return self.gcdOfStrings(str1[len(str2):], str2)
        else: return ''