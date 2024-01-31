# Valid Parentheses -> Python3

'''
Explanation: Use array as stack and dict where keys have closing and values have opening brackets. 
Run a loop for entire string. Check condition if char is in dict values and append in stack. Check 
in else if condition char present in dict keys. If stack if empty or dict char is not equal to 
stack pop return false. In outer else condition return false. Else valid.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        arr, dictVal = [], {')':'(','}':'{',']':'['}
        for i in s:
            if i in dictVal.values(): arr.append(i)
            elif i in dictVal.keys():
                if arr == [] or dictVal[i] != arr.pop(): return False
            else: return False
        return arr == []