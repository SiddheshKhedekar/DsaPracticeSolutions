# Subsets II -> Python3

'''
Explanation: Set res as empty array and call dfs with sorted nums, empty array and res. Inside dfs 
append route to res and run loop for x in range len nums. Inside check if x is greater than 0 and 
if nums at x is same at nums at x - 1 to continue otherwise call dfs with nums at x + 1 to end, 
route + nums at x as arrayitem and res.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, route, res):
            res.append(route)
            for x in range(len(nums)):
                if x > 0 and nums[x] == nums[x - 1]: continue
                dfs(nums[x + 1:], route+[nums[x]], res)
        dfs(sorted(nums), [], res)
        return res