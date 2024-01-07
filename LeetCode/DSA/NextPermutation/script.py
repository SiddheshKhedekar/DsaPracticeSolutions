# Next Permutation -> Python3

'''
Explanation: Brute force approach three loops. Find all possible combinations and then sort and 
select next. Slightly better approach is to use only inbuilt iteration functions. Best approach is 
to assign i and j as len of array. First traversal from reverse in while loop where i is greater 
than 0 and value at i is les than equal to value at i-1. Keep decrementing i. Check if i is 0 if 
yes than reverse entire list else run loop while value at j is less than value at k where k is i-1. 
Keep decrementing j in loop. Swap value at j and k. Reverse the list after k+1 index.
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        x = y = len(nums) - 1
        while x > 0 and nums[x] <= nums[x - 1]: x -= 1
        if x == 0:
            nums.reverse()
            return
        z = x - 1
        while nums[y] <= nums[z]: y -= 1
        nums[y],nums[z] = nums[z],nums[y]
        left, right = z + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1; right -= 1