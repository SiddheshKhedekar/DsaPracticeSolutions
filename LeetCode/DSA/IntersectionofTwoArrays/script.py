# Intersection of Two Arrays -> Python3

'''
Explanation: Return the list of set nums1 and set nums2.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))