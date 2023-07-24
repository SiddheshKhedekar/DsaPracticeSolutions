# Pow(x, n) -> Python3

'''
Explanation: Check if not n return 1 and check if n is less than 0 to return 1 divided by recursive 
call to myPow with x, -n. Check if n mod by 2 to return x multiplied by recursive call to myPow 
with x, n-1 and finally return recursive call to myPow with x multiplied by itself, n divide by 2.
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        if n % 2: return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)