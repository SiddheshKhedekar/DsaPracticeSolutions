# Multiply Strings -> Python3

'''
Explanation: Set ans as array of 0 which has size len num1 + len num2. Then run nested enumerated 
reversed loops on num1 and num2. Inside get the product of first characters after int conversion 
and save to index x+y and after saving the product value floor division at x+y+1 index mod the 
value at x+y index. Run while loop outside to pop the ending 0. And return the string of array in 
reversed order.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0] * (len(num1) + len(num2))
        for x, a in enumerate(reversed(num1)):
            for y, b in enumerate(reversed(num2)):
                ans[x+y] += int(a) * int(b)
                ans[x+y+1] += ans[x+y]//10
                ans[x+y] %= 10
        while len(ans) > 1 and ans[-1] == 0: ans.pop()
        return ''.join(map(str,ans[::-1]))