# Evaluate Reverse Polish Notation -> Python3

'''
Explanation: Define a stack and if not operators then appent the int values in it. Else pop the 
stack values in right and left and as per operator perform operation and append back to stack.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/": stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+": stack.append(l+r)
                elif t == "-": stack.append(l-r)
                elif t == "*": stack.append(l*r)
                else: stack.append(int(float(l)/r))
        return stack.pop()