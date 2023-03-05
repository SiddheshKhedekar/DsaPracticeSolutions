# Minimum Remove to Make Valid Parentheses -> Python3

'''
Explanation: Convert str to array and initialize stack, loop on enumerated array and check if char 
is opening ( and append index to array elseif char is ) then check if stack and pop else set array 
at index to ''. Run while loop on stack to set array at stack pop index to '' then join and return.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stra, stk = list(s), []
        for x, ch in enumerate(stra):
            if ch == '(': stk.append(x)
            elif ch == ')':
                if stk: stk.pop()
                else: stra[x] = ''
        while stk: stra[stk.pop()] = ''
        return ''.join(stra)