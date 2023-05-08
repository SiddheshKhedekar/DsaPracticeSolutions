# Sign of the Product of an Array -> Python3

'''
Explanation: Set res as 1 and then loop for i in nums. Check if i is 0 then return 0 also check if 
i is less than 0 and multiply ans by -1.
'''

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            if i == 0: return 0
            if i < 0: res *= -1
        return res