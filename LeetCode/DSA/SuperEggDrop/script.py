# Super Egg Drop -> Python3

'''
Explanation: Set dp and m to [0,0] and 0, in while loop till dp[-1] < n run a for loop in range 
len dp - 1 to 0 and increment dp[i] += dp[i-1]+1. If len dp < k+1 then do dp append(dp[-1]). 
Increment m by 1 and finally return m.
'''

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp, m = [0,0], 0
        while dp[-1] < n:
            for i in range(len(dp)-1, 0, -1): dp[i] += dp[i-1]+1
            if len(dp) < k +1: dp.append(dp[-1])
            m += 1
        return m