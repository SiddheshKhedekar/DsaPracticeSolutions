# Maximize Score After N Operations -> Python3

'''
Explanation: In main function return the dfs call to 1, 0 and initialise dfs function with x, mask 
and cache the function. Inside dfs check if x is greater than len nums floor div by 2 and return 0 
then set ans as 0. Then run for loop on range len nums as i and run for loop nested inside on range 
i + 1 to len nums as j. Inside set new_mask as 1 << i + 1 << j and if not mask & new_mask then set 
and as max of ans, x multiplied by the gcd of nums at i, nums at j + the dfs call to x+ 1 and mask 
+ new_mask then outside loops return ans.
'''

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(x, mask):
            if x > len(nums) // 2: return 0
            ans = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    new_mask = (1 << i) + (1 << j)
                    if not mask & new_mask:
                        ans = max(ans, x * gcd(nums[i], nums[j]) + dfs(x + 1, mask + new_mask))
            return ans
        return dfs(1, 0)