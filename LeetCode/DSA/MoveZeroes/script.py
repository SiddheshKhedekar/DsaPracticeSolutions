# Move Zeroes -> Python3

'''
Explanation: Use read and write pointers where write set to 0 and use read to loop for range len 
nums. Inside check if value at read is not 0 and that at write is to swap the values at pointer 
then check if value at write is not 0 to increment write by 1.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        writePointer = 0
        for readPointer in range(len(nums)):
            if nums[readPointer] != 0 and nums[writePointer] == 0:
                nums[writePointer], nums[readPointer] = nums[readPointer], nums[writePointer]
            if nums[writePointer] != 0: writePointer+=1