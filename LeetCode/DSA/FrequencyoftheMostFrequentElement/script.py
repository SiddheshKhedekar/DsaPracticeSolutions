# Frequency of the Most Frequent Element -> Python3

'''
Explanation: Set sliding window start as x and sot the list. Run loop for y in range of len nums 
and increment k by nums at y then check if k is less than nums at y multiplied by y - x + 1 as 
whole. Inside condition check decrement k by nums at x and increment x by 1 and finally return 
y - x + 1.
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        x = 0
        nums.sort()
        for y in range(len(nums)):
            k += nums[y]
            if k < nums[y] * (y - x + 1):
                k -= nums[x]
                x += 1
        return y - x + 1