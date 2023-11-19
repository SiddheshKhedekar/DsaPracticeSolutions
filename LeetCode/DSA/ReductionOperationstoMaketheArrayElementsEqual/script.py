# Reduction Operations to Make the Array Elements Equal -> Python3

'''
Explanation: Sort the array and set res, valu as 0 then loop on range from 1 to len nums. Inside 
check if nums as x-1 is less than nums at x then increment valu by 1 and for each loop increment 
res by valu then at end of loop return res.
'''

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = valu = 0
        nums.sort()
        for x in range(1, len(nums)):
            if nums[x - 1] < nums[x]: valu += 1
            res += valu
        return res