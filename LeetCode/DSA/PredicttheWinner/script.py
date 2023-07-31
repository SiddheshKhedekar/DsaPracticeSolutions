# Predict the Winner -> Python3

'''
Explanation: Search for the max difference between player 1 and 2 then return the difference if 
greater than or same as 0. Use dp as dict to keep track of differences and write search function to 
get the max difference.
'''

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def search(x, y):
            if (x, y) not in dp:
                if x == y: return nums[x]
                dp[x, y] = max(nums[x] - search(x + 1, y), nums[y] - search(x, y - 1))
            return dp[x, y]
        return search(0, len(nums) - 1) >= 0