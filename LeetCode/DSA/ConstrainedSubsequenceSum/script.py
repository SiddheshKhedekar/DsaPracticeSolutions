# Constrained Subsequence Sum -> Python3

'''
Explanation: Initialize deque as dq, then run a loop on range of len nums with index x. For each 
iteration, increment value of num at x by dq at 0 if dq exists else 0. Then run the loop while len 
of dq and nums at x is greater than dp at -1 to pop dq. After while loop ends, check if nums at x 
is greater than 0 to append it to dq. Then check if x is greater than k and dq exists, and dq at 0 
is the same as nums at x - k to popleft dq, and finally return max of nums at end of for loop.
'''

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        for x in range(len(nums)):
            nums[x] += dq[0] if dq else 0
            while len(dq) and nums[x] > dq[-1]: dq.pop()
            if nums[x] > 0: dq.append(nums[x])
            if x >= k and dq and dq[0] == nums[x - k]: dq.popleft()
        return max(nums)