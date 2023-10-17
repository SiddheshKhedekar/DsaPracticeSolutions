# Permutations II -> Python3

'''
Explanation: Set res as array of single empty array and run loop for num in nums. Set new_res as 
empty array and run loop for r in res and another loop inside for index in range len r + 1. Inside 
append r upto index + num as array item + r from index to end into new_res. Then check if index is 
less than r and r at index is num and break and outside inner two loops set res as new_res.
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_res = []
            for r in res:
                for indx in range(len(r) + 1):
                    new_res.append(r[:indx] + [num] + r[indx:])
                    if indx < len(r) and r[indx] == num: break
            res = new_res
        return res