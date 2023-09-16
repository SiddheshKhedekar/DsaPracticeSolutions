# Add Binary -> Python3

'''
Explanation: Set res, i, j, carry to '', len a-1, len b-1, 0. While i >=0 or j >= 0 and inside set 
summ to carry if i >= 0 set sum += ord(a[i])-ord(‘0’) and same for j. Decrement i and j by 1 and 
set carry to 1 if summ > 1 else 0 and increment res by str(summ%2). Out of loop check if carry != 0 
increment res += str(carry) and return res[::-1].
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, i, j, carry = '', len(a)-1, len(b)-1, 0
        while i >= 0 or j >= 0:
            summ = carry
            if i >= 0: summ += ord(a[i]) - ord('0')
            if j >= 0: summ += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if summ > 1 else 0
            res += str(summ % 2)
        if carry != 0: res+= str(carry)
        return res[::-1]