# Find First and Last Position of Element in Sorted Array -> Python3

'''
Explanation: Use sub function search taking n as input inside set lo and hi to 0 and len(nums). Run 
while loop for lo < hi set mid to (lo+hi)//2. Check if nums[mid] >= n and set hi to mid else set lo 
to mid+1. Out of loop return lo. In main function set lo to search(target) and return array of lo 
and search(target+1)-1 only if target is in nums[lo:lo+1] else [-1,-1].
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo+hi)//2
                if nums[mid] >= n: hi = mid
                else: lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1,-1]