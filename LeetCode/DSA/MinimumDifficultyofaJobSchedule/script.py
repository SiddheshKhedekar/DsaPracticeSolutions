# Minimum Difficulty of a Job Schedule -> Python3

'''
Explanation: Set n to len of jd, if n < d then return -1, set dp dp2 to [float inf]*n, [0]*n and 
run a for loop in range d. Inside initialize empty stack and run another for loop in range d,n. Set 
dp2 to dp[i-1]+jd[i] if i else jd[i]run while loop till stack and jd[stack[-1]]<=jd[i]. Inside set 
j to stack.pop and dp2 = min of dp2[i], dp[j]-jd[j]+jd[i]. If stack set dp2 to min of dp2[i], 
dp2[stack[-1]]. Append i to stack and outside inner for swap dp and dp2 values finally returning 
dp[-1] outside for loop.
'''

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1
        dp, dp2 = [float('inf')]*n, [0]*n
        for d in range(d):
            stack = []
            for i in range(d,n):
                dp2[i] = dp[i-1] + jobDifficulty[i] if i else jobDifficulty[i]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    dp2[i] = min(dp2[i],dp2[j]-jobDifficulty[j]+jobDifficulty[i])
                if stack: dp2[i] = min(dp2[i],dp2[stack[-1]])
                stack.append(i)
            dp, dp2 = dp2, dp
        return dp[-1]