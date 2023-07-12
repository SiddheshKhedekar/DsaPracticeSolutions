# Next Greater Element III -> Python3

'''
Explanation: Our goal is to find next number with the same digits, which is greater than given one 
and which is the smallest one. It makes sense to try to take our number as close to original one as 
possible. We start from the end and look for increasing pattern. In case all number has increasing 
pattern, there is no bigger number with the same digits, so we can return -1. Then we need to find 
the first digit in our ending, which is less or equal to digits[i-1] and we look for the next 
number with the same digits. We then swap the numbers. Finally, we need to reverse last digits.
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        x = len(nums) - 1
        while x - 1 >= 0 and nums[x] <= nums[x - 1]: x -= 1
        if x == 0: return -1
        y = x
        while y + 1 < len(nums) and nums[y + 1] > nums[x - 1]: y += 1
        nums[x - 1], nums[y] = nums[y], nums[x - 1]
        nums[x:] = nums[x:][::-1]
        res = int(''.join(nums))
        return res if res < 1<<31 else -1