# Special Array With X Elements Greater Than or Equal X -> Python3

'''
Explanation: Use Binary search, first sort in reverse order and then take l and r as o and len 
nums. While l<r set mid to l+(r-l)//2 amd check if nums[m] > m to update l to m+1 else r = m and 
return -1 if l < len(nums) and l == nums[l] else l.
'''

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l)//2
            if nums[m] > m: l = m + 1
            else: r = m
        return -1 if l < len(nums) and l == nums[l] else l