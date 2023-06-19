# Find All Numbers Disappeared in an Array -> Python3

'''
Explanation: Use original array to find. First loop traverse through the array. Get abs value -1 in 
temp and check if value at index temp is positiveand in condition negate the number. Second 
traversal if value is positive append the index+1 value in result.
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0: nums[temp] *= -1
        for i,j in enumerate(nums):
            if j > 0: arr.append(i+1)
        return arr