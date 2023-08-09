# Minimize the Maximum Difference of Pairs -> Python3

'''
Explanation: To compare differences, we sort the array. Set len, left and right then run a loop 
while left is less than right and set mid along with c, x as 0, 1. Again run loop while x is less 
than len and inside check if difference in element at x and its previous is less than or same as 
mid to increment both c, x otherwise only x. Outside of inner loop check if c is less than or the 
same as p to set right as mid else left will be mid and finally out of loop return left.
'''

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, lft, rgt = len(nums), 0, nums[-1] - nums[0]
        while lft < rgt:
            m = (lft + rgt) // 2
            c, x = 0, 1
            while x < l:
                if nums[x] - nums[x - 1] <= m:
                    c += 1
                    x += 1
                x += 1
            if c >= p: rgt = m
            else: lft = m + 1
        return lft