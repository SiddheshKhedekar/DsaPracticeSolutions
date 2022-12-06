# Contains Duplicate -> Python3

'''
Explanation: Use dictionary as it is faster to search than list. Check if number in dictionary.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = {}
        for i in nums:
            if i in new: return True
            else: new[i] = 1
        return False