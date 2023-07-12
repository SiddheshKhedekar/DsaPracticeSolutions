# Next Greater Element II -> Python3

'''
Explanation: We can loop once and get the next greater number of a normal array. By looping twice, 
we can get the next greater number of a circular array. In first loop we multiply the list of range 
and in inner loop check for stack and nums value at last stk value compared to nums at x. Inside 
the loop set the ans at stk pop as nums value at x and in outer loop append x to stack.
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk, ans = [], [-1] * len(nums)
        for x in list(range(len(nums))) * 2:
            while stk and (nums[stk[-1]] < nums[x]): ans[stk.pop()] = nums[x]
            stk.append(x)
        return ans