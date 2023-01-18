# Find Pivot Index -> Python3

'''
Explanation: Get the total sum and loop on nums. Check where left sum equals total sum minus left 
sum and current value and then return index.
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totSum, leftSum = sum(nums), 0
        for i, j in enumerate(nums):
            if leftSum == (totSum - leftSum - j): return i
            leftSum += j
        return -1