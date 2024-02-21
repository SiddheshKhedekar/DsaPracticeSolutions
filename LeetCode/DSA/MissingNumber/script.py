# Missing Number -> Python3

'''
Explanation: Return the pop on the set of range len nums + 1 after subtracting the set of nums.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums) + 1)) - set(nums)).pop()