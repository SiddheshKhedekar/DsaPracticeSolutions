# Remove All Adjacent Duplicates In String -> Python3

'''
Explanation: Use stack, iterate on all chars in str and pop the last element if duplicate in stack 
else append and after loop end join and return.
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c: stack.pop()
            else: stack.append(c)
        return ''.join(stack)