# Jump Game -> Python3

'''
Explanation: Set max index as goal. Traverse indexes in reverse order and check if index 
plus value at index >= goal and set goal = i. Finally return not goal.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums))[::-1]:
            if i+nums[i] >= goal: goal = i
        return not goal