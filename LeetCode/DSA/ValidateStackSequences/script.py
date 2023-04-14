# Validate Stack Sequences -> Python3

'''
Explanation: Run a for loop and append pushed elements in stk. Inside run loop while len of stack 
is greater than 0 and last element of stack is ith element of popped to pop the stk and increment i 
by 1. Return true if len stk is 0 else false.
'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk, x = [], 0
        for num in pushed:
            stk.append(num)
            while len(stk) > 0 and stk[len(stk) - 1] == popped[x]:
                stk.pop()
                x += 1
        return True if len(stk) == 0 else False