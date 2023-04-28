# Product of Array Except Self -> Python3

'''
Explanation: Set ans as array of 1 which has len same as nums and suf, pre as 1. Then run a for 
loop on range of len nums and multiply the ans at i by the pre and multiply ans at -1-i by suf. We 
also multiply pre by the nums at i and suf as the nums at -1-i.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, suf, pre = [1] * len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1-i] *= suf
            suf *= nums[-1-i]
        return ans