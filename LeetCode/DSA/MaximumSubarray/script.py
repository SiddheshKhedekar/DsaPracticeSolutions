# Maximum Subarray -> Python3

'''
Explanation: Brute force approach three loops. Top one for start of sub array. Middle to get end 
and last one to get sum in subarray. Compare and set max.Slightly better approach is to use only 
two loops and use prebuilt sum function. Best approach is to use Kadane’s Algorithm which makes use 
of meh starting from 0 and msf the min value possible. In a single for loop add current index value 
to meh and check if meh is greater than msf. If yes than msf becomes meh. If meh is less than 0 
then meh is 0. After loop return msf.

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msf, meh = -inf, 0
        for i in nums:
            meh = max(i, meh + i)
            msf = max(msf, meh)
        return msf