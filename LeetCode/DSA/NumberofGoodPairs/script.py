# Number of Good Pairs -> Python3

'''
Explanation: Set count as 0 then loop for len nums and inside nest for loop starting from i. Check 
if nums at i and j are same to increment count. At the end of both loops return count.
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]: count+=1
        return count