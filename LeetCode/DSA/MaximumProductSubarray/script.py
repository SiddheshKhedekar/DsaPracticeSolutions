# Maximum Product Subarray -> Python3

'''
Explanation: Save reverse of array in temp. Save prefix product in original and suffix product in 
temp. Return max of the sum of both arrays.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums1 = nums[::-1]
        for x in range(1, len(nums)):
            nums[x] *= nums[x - 1] or 1
            nums1[x] *= nums1[x - 1] or 1
        return max(nums + nums1)