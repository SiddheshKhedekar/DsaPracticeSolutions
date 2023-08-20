# Combination Sum II -> Python3

'''
Explanation: Sort candidates and initialse ans as empty array then call combinesum with candidates, 
0, empty array, ans, target. Inside combinesum check if not target to append path to ans and 
return. Then run loop for index in range start to len nums and check if index is greater than start 
and nums at index is same as nums at previous index to continue. Check if nums at index is greater 
than target to break then call combinesum recursively with nums, next index, path + nums at index 
as array, ans, target - nums at index.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def combineSum(nums, start, path, ans, target):
            if not target: 
                ans.append(path)
                return
            for indx in range(start, len(nums)):
                if indx > start and nums[indx] == nums[indx - 1]: continue
                if nums[indx] > target: break
                combineSum(nums, indx + 1, path + [nums[indx]], ans, target - nums[indx])
        combineSum(candidates, 0, [], ans, target)
        return ans