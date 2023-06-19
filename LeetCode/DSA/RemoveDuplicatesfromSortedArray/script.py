# Remove Duplicates from Sorted Array -> Python3

'''
Explanation: Two pointer method. Assign count from second index. Loop from second index to the end. 
Check for condition of i-1 idex and i index not having same value. In condition assign the count 
index value and update count. Get unique length and del the rest. 
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[count] = nums[i]
                count+=1
        count = len(nums)-count
        for i in range(0,count): del nums[-1]