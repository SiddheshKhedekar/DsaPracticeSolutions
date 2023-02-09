# Jump Game II -> Python3

'''
Explanation: Check for minimum constraint, set l, r and times to 0, nums[0] and 1, run loop while r 
less than length of mums and increment times. Also set nxt to max of i+nums[i] in range l to r+1 
and swap l, r with r, nxt.
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r, times = 0, nums[0], 1
        while r < len(nums)-1:
            times+=1
            nxt = max(i + nums[i] for i in range(l, r+1))
            l, r = r, nxt
        return times