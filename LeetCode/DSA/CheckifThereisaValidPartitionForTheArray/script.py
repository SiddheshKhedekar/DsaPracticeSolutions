# Check if There is a Valid Partition For The Array -> Python3

'''
Explanation: Implement rolling dp where dp at i mod 4 defines if there is partition from 0 to i. 
Iterate over len of nums and inside set dp at x mod 4 at false. Check if nums at i and i - 1 are 
exactly same to set dp at i as or of itself and dp at i - 2. Then check if nums at i, i - 1 and 
i - 2 are equal to set dp at i as or of itself and dp at 1 - 3 and same if they are consecutive. 
Finally return dp at n - 1.
'''

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        l, dp = len(nums), [False, False, False, True]
        for x in range(l):
            dp[x % 4] = False
            if x - 1 >= 0 and nums[x] == nums[x - 1]:
                dp[x % 4] |= dp[(x - 2) % 4]
            if x - 2 >= 0 and nums[x] == nums[x - 1] == nums[x - 2]:
                dp[x % 4] |= dp[(x - 3) % 4]
            if x - 1 >= 0 and nums[x] == nums[x - 1] + 1 == nums[x - 2] + 2:
                dp[x % 4] |= dp[(x - 3) % 4]
        return dp[(l - 1) % 4]