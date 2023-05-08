# Find the Difference of Two Arrays -> Python3

'''
Explanation: Save the set of arrays as set1 and set2 then subtract the sets from each other and 
return after formatting as list.
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]