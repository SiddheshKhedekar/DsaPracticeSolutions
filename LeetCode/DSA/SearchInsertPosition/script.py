# Search Insert Position -> Python3

'''
Explanation: Use binary search to find the index of the array needed and return it.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            m = (start + end) // 2
            if nums[m] < target: start = m + 1
            else:
                if nums[m] == target and nums[m - 1] != target: return m
                else: end = m - 1
        return start