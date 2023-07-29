# Soup Servings -> Python3

'''
Explanation: Initialize mem as dict and check if n is beyond 4800 then probability is always 1 so 
return same. Then set n as the ceil of n divided by 25.0 and return the call to func with n as both 
params. In func check if both params in mem to return the vault at params then check if both params 
less than or same as 0 to return 0.5. Also check if x is less than 0 to return 1 and y is less than 
0 to return 0. Set mem at x, y as  0.25 multiplied by the sum of func call for x, y subtracting 4 
to 0 in combination then return mem at x,y.
'''

class Solution:
    def soupServings(self, n: int) -> float:
        mem = {}
        if n > 4800: return 1
        def func(x, y):
            if (x, y) in mem: return mem[x, y]
            if x <= 0 and y <= 0: return 0.5
            if x <= 0: return 1
            if y <= 0: return 0
            mem[(x, y)] = 0.25 * (func(x - 4, y) + func(x - 3, y - 1) + func(x - 2, y - 2) + \
            func(x - 1, y - 3))
            return mem[(x, y)]
        n = math.ceil(n / 25.0)
        return func(n, n)