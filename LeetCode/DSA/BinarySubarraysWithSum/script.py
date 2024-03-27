# Binary Subarrays With Sum -> Python3

'''
Explanation: Return the value of func with goal - func with goal - 1. Inside func first check if 
goal is less than 0 to return 0 then set ans, x to 0. Then loop on range len nums decrement goal by 
nums at y and run another loop while goal is less than 0. Inside increment goal by nums at x and x 
by 1 then out of this loop increment ans by y - x + 1 and return ans out of upper loop.
'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def func(goal):
            if goal < 0: return 0
            ans = x = 0
            for y in range(len(nums)):
                goal -= nums[y]
                while goal < 0:
                    goal += nums[x]
                    x += 1
                ans += y - x + 1
            return ans
        return func(goal) - func(goal - 1)