# Minimum Average Difference -> Python3

'''
Explanation: Calculate the sumend first and then iterate on length and add to sumfront while 
subtracting from sumend. Get the averages for front, end as defined and then get the least absolute 
difference and set index.
'''

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sumEnd, sumFront, res, diff, n = 0, 0, 0, 1e9, len(nums)
        for num in nums: sumEnd += num
        for i in range(n):
            sumFront += nums[i]
            sumEnd -= nums[i]
            avg1 = sumEnd//(n-1-i) if i != n-1 else 0 
            avg2 = sumFront//(i+1)
            if abs(avg1 - avg2) < diff:
                diff = abs(avg1 - avg2)
                res = i
        return res