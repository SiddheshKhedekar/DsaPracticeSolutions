# Number of Subsequences That Satisfy the Given Sum Condition -> Python3

'''
Explanation: Sort nums and then set left as 0, right as len nums and modulo as given. Run loop 
while left is less than equal as right and check if nums left plus nums right is greater than 
target to decrement right by 1. Else increment ans by the pow of2, right -left, modulo and 
increment left. Finally return ans after modulo.
'''

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right, ans, modulo = 0, len(nums) - 1, 0, 10**9 + 7
        while left <= right:
            if nums[left] + nums[right] > target: right -= 1
            else:
                ans += pow(2, right - left, modulo)
                left += 1
        return ans % modulo