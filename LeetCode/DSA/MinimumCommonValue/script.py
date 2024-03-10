# Minimum Common Value -> Python3

'''
Explanation: Return the min of set nums1 and set nums2 where default is -1.
'''

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default = -1)