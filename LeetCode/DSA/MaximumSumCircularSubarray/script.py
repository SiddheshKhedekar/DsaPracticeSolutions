# Maximum Sum Circular Subarray -> Python3

'''
Explanation: In case of circular array we can get max subarray sum by subtracting min subarray sum 
from the total sum. We handle edge case of negative array be checking if max sum is greater than 0. 
'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        tot, mxSum, cMax, mnSum, cMin = 0, nums[0], 0, nums[0], 0
        for num in nums:
            cMax = max(cMax + num, num)
            mxSum = max(mxSum, cMax)
            cMin = min(cMin + num, num)
            mnSum = min(mnSum, cMin)
            tot += num
        return max(mxSum, tot - mnSum) if mxSum > 0 else mxSum