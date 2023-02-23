# Combination Sum -> Python3

'''
Explanation: Define a dfs function and check if the target is less than 0. If target is 0 then 
append path to res and then run a for loop on nums length and call dfs function passing the nums i 
to end elements, target minus nums i and pass path as path plus nums i as array.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums, target, p, res):
            if target < 0: return
            if target == 0: 
                res.append(p)
                return
            for i in range(len(nums)):
                dfs(nums[i:], target-nums[i], p+[nums[i]], res)
        dfs(candidates, target, [], res)
        return res