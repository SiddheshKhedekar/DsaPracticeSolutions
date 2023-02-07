# Valid Perfect Square -> Python3

'''
Explanation: Use math by setting temp to 1 and inside loop for n > 0 decrementing n by temp and 
incrementing temp by 2 and finallly return n == 0.
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        temp = 1
        while num > 0:
            num-=temp 
            temp+=2
        return num == 0