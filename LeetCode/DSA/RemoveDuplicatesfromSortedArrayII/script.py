# Remove Duplicates from Sorted Array II -> Python3

'''
Explanation: Set i as 0 and loop on n in nums then check if i is less than 2 or n is greater than 
nums at i - 2 to reassign nums at i as n and increment i by i. Finally return i outside loop.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]: nums[i], i = n, i + 1
        return i