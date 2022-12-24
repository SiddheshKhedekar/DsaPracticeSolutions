# Basic Calculator -> Python3

'''
Explanation: Write a calc function that takes index and run loop till len of string. For digits do 
appropriate processing else if operand call the update function else if ( then cal calc again and 
if ) then call update. In update function check the operator and append to stack after processing. 
Inside calc again set num and sign and update again return sum in stack.
'''

class Solution:
    def calculate(self, s: str) -> int:
        def calc(it):
            def update(op, v):
                if op == '+': stack.append(v)
                if op == '-': stack.append(-v)
            num, stack, sign = 0, [], '+'
            while it < len(s):
                if s[it].isdigit(): num = num * 10 + int(s[it])
                elif s[it] in '+-': 
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == '(': 
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ')': 
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)
        return calc(0)