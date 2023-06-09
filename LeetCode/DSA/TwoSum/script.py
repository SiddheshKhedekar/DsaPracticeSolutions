# Two Sum -> Python3

'''
Explanation: Use dp by saving visited in mem dictonary. Run a loop where i, j in enumerate of nums. 
Save the difference in target and nums i in res and check if res in mem. If true return 
[i, mem[res]] else set mem[j] to i.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, j in enumerate(nums):
            rem = target - nums[i]
            if rem in mem: return [i, mem[rem]]
            else: mem[j] = i