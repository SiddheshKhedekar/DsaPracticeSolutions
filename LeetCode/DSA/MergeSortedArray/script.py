# Merge Sorted Array -> Python3

'''
Explanation: Assign x, y, z as the last index of the two arrays and the merged one. Run loop while 
y is greater than or same as 0 and inside check whichever array item at index is greater to assign 
it to the merged array and decrement corresponding index.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y, z = m - 1, n - 1, m + n - 1
        while y >= 0:
            if x >= 0 and nums1[x] > nums2[y]: nums1[z], x = nums1[x], x - 1
            else: nums1[z], y = nums2[y], y - 1
            z -= 1