# Subarrays with K Different Integers -> Python3

'''
Explanation: Implement a helper function that uses sliding window and in main function return func 
of nums, k - the func value of nums, k - 1. In helper set cnt as counter and ans, x as 0. Loop y on 
range len nums and check if cnt at numx y is 0 to decrement k next increment cnt at same. Loop 
while k < 0 to decrement cnt at nums x and if cnt at same is 0 increment k next increment x and out 
of while increment ans by y - x + 1. Finally return ans at end of for loop.
'''

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def func(nums, k):
            cnt, ans, x = Counter(), 0, 0
            for y in range(len(nums)):
                if cnt[nums[y]] == 0: k -= 1
                cnt[nums[y]] += 1
                while k < 0:
                    cnt[nums[x]] -= 1
                    if cnt[nums[x]] == 0: k += 1
                    x += 1
                ans += y - x + 1
            return ans
        return func(nums, k) - func(nums, k - 1)