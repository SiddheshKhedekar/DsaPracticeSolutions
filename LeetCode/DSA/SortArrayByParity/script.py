# Sort Array By Parity -> Python3

'''
Explanation: Use two pointers, traverse using read pointer and incrementing write pointer post swap 
when condition is met.
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        writePointer = 0
        for readPointer in range(0,len(nums)):
            if nums[readPointer]%2 == 0:
                nums[readPointer], nums[writePointer] = nums[writePointer], nums[readPointer]
                writePointer+=1
        return nums