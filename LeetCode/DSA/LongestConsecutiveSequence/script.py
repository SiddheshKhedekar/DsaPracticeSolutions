# Longest Consecutive Sequence -> Python3

'''
Explanation: Set nums as set of it and res as 0 then loop for i in nums and check if i - 1 is not 
in nums. If true then set j as i + 1 and run loop while j is in nums to increment j by 1 then set 
res as the max of itself and j - i. Finally return res at end of loop. What we check is that no 
series repeated and max count saved in res.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, res = set(nums), 0
        for i in nums:
            if i - 1 not in nums:
                j = i + 1
                while j in nums: j += 1
                res = max(res, j - i)
        return res