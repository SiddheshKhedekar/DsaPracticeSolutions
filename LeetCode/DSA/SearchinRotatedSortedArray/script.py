# Search in Rotated Sorted Array -> Python3

'''
Explanation: If not nums return -1 and then set l, h to 0,len(nums)-1. Run loop while l <= h and 
inside set mid to l+h//2 if target is nums[mid] return mid. Two conditions first where the low 
value is less than mid and in other opposite. Inside first condition again to be checked if target 
between low and mid in order and in other check if target between mid and high. In first condition 
high is set to mid-1 and else low set to mid+1. In alternate condition low is set to mid +1 and 
else high to mid-1.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if target == nums[mid]: return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]: high = mid-1
                else: low = mid+1
            else:
                if nums[mid] <= target <= nums[high]: low = mid+1
                else: high = mid-1
        return -1