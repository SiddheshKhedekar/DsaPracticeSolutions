# Length of Longest Subarray With at Most K Frequency -> Python3

'''
Explanation: Set count as dict to save the frequency of elements and ans, x as 0. Loop on range len 
nums to update count and if an element has frequency bigger than k, decrement the left side of 
window until it is not. Then update ans as size of longest good subarray using max of ans and 
y - x + 1 and return ans at end.
'''

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count, ans, x = Counter(), 0, 0
        for y in range(len(nums)):
            count[nums[y]] += 1
            while count[nums[y]] > k:
                count[nums[x]] -= 1
                x += 1
            ans = max(ans, y - x + 1)
        return ans