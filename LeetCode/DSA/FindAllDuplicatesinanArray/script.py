# Find All Duplicates in an Array -> Python3

'''
Explanation: Set ans as empty array then loop on i in nums to check if nums at abs i after -1 is 
less than 0 to append the abs value of i in ans else set nums at abs of i after -1 as its negative 
value. At end of loop return ans.
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums[abs(i) - 1] < 0: ans.append(abs(i))
            else: nums[abs(i) - 1] *= -1
        return ans