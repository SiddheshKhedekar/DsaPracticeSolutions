# Find Polygon With the Largest Perimeter -> Python3

'''
Explanation: Sort nums and then set crnt as the sum of it. Loop while nums and crnt is less than or 
same as last element in nums * 2 to decrement crnt by nums pop. Finally return the sum of nums if 
len nums is greater than 2 else return -1.
'''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        crnt = sum(nums)
        while nums and crnt <= nums[-1] * 2: crnt -= nums.pop()
        return sum(nums) if len(nums) > 2 else -1