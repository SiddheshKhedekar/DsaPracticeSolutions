# Number of Dice Rolls With Target Sum -> Python3

'''
Explanation: Use dp by first setting dictionary memo and defining a dp function. In dp function 
first check if n is 0 and return 0 if target > 0 else 1. Again check if (n,target) in memo and 
return memo[(n,target)]. Set to_return to 0 and run loop for i in range(max(0,target-k), target). 
Inside loop increment to_return by dp(n-1, i) call. Outside set memo[(n, target)] to to_return and 
return to_return. In main function return the dp(n, target) modulo value asked.
'''

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dp(n, target):
            if n == 0: return 0 if target > 0 else 1
            if (n, target) in memo: return memo[(n, target)]
            to_return = 0
            for i in range(max(0,target-k), target): to_return += dp(n-1, i)
            memo[(n, target)] = to_return
            return to_return
        return dp(n, target) % (10**9 + 7)