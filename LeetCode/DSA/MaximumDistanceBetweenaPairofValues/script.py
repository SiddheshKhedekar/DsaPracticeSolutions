# Maximum Distance Between a Pair of Values -> Python3

'''
Explanation: Set i = j = res = 0 and run while loop for i < len(nums1) and j < len(nums2). Check if 
nums1 i > nums2 j value and increment i by 1 else set res to max of res and j-i also increment j. 
Outside loop return res.
'''

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]: i+=1
            else:
                res = max(res, j-i)
                j+=1
        return res