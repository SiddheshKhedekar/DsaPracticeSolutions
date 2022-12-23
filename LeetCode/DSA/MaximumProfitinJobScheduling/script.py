# Maximum Profit in Job Scheduling -> Python3

'''
Explanation: Sort jobs by starttime, endtime and profit then set memory and loop of jobs. Check 
with last element in memory if we make more money we do the job and add pair of [e, cur] to the 
end of memory else we do'nt do the job.
'''

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0,0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s+1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]