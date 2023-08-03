# Wiggle Subsequence -> Python3

'''
Explanation: Check if input is valid then set len and increasing flag as ln, wgl. Loop on nums and 
alternate wgl while incrementing ln and on loop end finally return ln.
'''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        ln, wgl = 1, None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and wgl != True:
                ln += 1
                wgl = True
            if nums[i] < nums[i - 1] and wgl != False:
                ln += 1
                wgl = False
        return ln