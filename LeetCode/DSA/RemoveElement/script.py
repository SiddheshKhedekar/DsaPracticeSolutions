# Remove Element -> Python3

'''
Explanation: Set index as 0 and run loop for range len nums. Check if nums at i is not val to set 
nums at i as nums at index then increment index and finally out of loop return index.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indx = 0
        for i in range(len(nums)):
            if nums[i] != val: nums[indx], indx = nums[i], indx + 1
        return indx