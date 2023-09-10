# Decode String -> Python3

'''
Explanation: Get stack, cn and cs as [], 0, ‘’ for c in s run loop and inside check if c is 
[ second time ] and third if is digit finally run else where cs incremented by c and finally out 
return cs. In first check append cs to stack and then same for cn and set cs and cn to base value. 
In second check pop stack and take in num and pop again and take in ps. Set cs to ps + num*cs and 
in isdigit check set cn to cn*10 + int c.
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack, curNum, curString = [], 0, ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit(): curNum = curNum*10 + int(c)
            else: curString += c
        return curString