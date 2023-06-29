# Shuffle an Array -> Python3

'''
Explanation: In init initialise nums, cpy and in reset set nums as cpy and return. In shuffle loop 
on length and set a random integer to swap values in the list before returning.
'''

class Solution:
    def __init__(self, nums: List[int]):
        self.nums, self.cpy = nums[:], nums[:]
    def reset(self) -> List[int]:
        self.nums = self.cpy[:]
        return self.nums
    def shuffle(self) -> List[int]:
        l = len(self.nums)
        for x in range(l):
            y = randint(x, l - 1)
            self.nums[x], self.nums[y] = self.nums[y], self.nums[x]
        return self.nums