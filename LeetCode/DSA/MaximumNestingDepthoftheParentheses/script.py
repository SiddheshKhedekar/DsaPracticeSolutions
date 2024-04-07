# Maximum Nesting Depth of the Parentheses -> Python3

'''
Explanation: Set ans and crnt as 0 then loop on all char in s to check if it is ‘(’ to increment 
crnt and set ans as max of itself and crnt. Then check if char is ‘)’ to decrement crnt and finally 
return ans out of loop.
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = crnt = 0
        for char in s:
            if char == '(':
                crnt += 1
                ans = max(ans, crnt)
            if char == ')': crnt -= 1
        return ans