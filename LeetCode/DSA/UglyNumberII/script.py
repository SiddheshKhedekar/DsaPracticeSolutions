# Ugly Number II -> Python3

'''
Explanation: Set unum as array of first ugly number and c2, c3, c5 as 0. Then run loop while n is 
greater than 1 and set u2, u3, u5 as the 2,3,5 * unum at c 2,3,5 from above. Then set umin as min 
of all u 2,3,5. Check if umin is u 2,3,5 and increment respective counter by 1 then append umin in 
unum and decrement n by 1 finally return last value at unum.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uNum, c2, c3, c5 = [1], 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * uNum[c2], 3 * uNum[c3], 5 * uNum[c5]
            uMin = min((u2, u3, u5))
            if uMin == u2: c2 += 1
            if uMin == u3: c3 += 1
            if uMin == u5: c5 += 1
            uNum.append(uMin)
            n -= 1
        return uNum[-1]