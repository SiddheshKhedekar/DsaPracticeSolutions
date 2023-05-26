# Uncrossed Lines -> Python3

'''
Explanation: Set dp, a, b as defaultdict int, len nums1, len nums2. Run loop on range a and inside 
loop on range b set dp at x, y as max of dp at x-1, y-1 + nums1 at x == nums2 at y or dp at x-1, y 
or dp at x, y-1. Then finally return dp at a-1, b-1
'''

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp, a, b = defaultdict(int), len(nums1), len(nums2)
        for x in range(a):
            for y in range(b):
                dp[x, y] = max(dp[x - 1, y - 1] + (nums1[x] == nums2[y]), dp[x - 1, y], \
                            dp[x, y - 1])
        return dp[a - 1, b - 1]