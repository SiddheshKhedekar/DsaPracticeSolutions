# K Radius Subarray Averages -> Python3

'''
Explanation: Define as as array of -1 of len nums and set left pointer along with diameter of 
window and curWinSum then loop on range len nums as r and keep incrementing curWinSum. Check if 
diameter is met and then set ans at index when condition met as curWinSum after floor division 
decrement curWinSum and update l.
'''

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans, l, curWinSum, d  = [-1] * len(nums), 0, 0, 2 * k + 1
        for r in range(len(nums)):
            curWinSum += nums[r]
            if (r - l + 1 >= d):
                ans[l + k] = curWinSum // d
                curWinSum -= nums[l]
                l += 1
        return ans