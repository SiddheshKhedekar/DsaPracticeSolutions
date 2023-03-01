# Permutations -> Python3

'''
Explanation: Define res as [] and call dfs function passing nums, [] as path and res and then 
return res. Define a dfs function where if not nums do res append path. Run loop on range len nums 
and call dfs by passing nums[:i] + nums[i+1:], path + [nums i] and res.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            if not nums: res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        res = []
        dfs(nums, [], res)
        return res