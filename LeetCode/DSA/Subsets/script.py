# Subsets -> Python3

'''
Explanation: Set res as empty array and call dfs with nums, empty array and res. Inside dfs append 
route in res and run loop for x in range len nums then call dfs with nums from x+1 to end, route + 
nums at x as arrayitem and res.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, route, res):
            res.append(route)
            for x in range(len(nums)):
                dfs(nums[x + 1:], route+[nums[x]], res)
        dfs(nums, [], res)
        return res