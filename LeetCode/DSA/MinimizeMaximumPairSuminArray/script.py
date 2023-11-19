# Minimize Maximum Pair Sum in Array -> Python3

'''
Explanation: By sorting the array and creating pairs of min, max then fetching max from the pairs 
we can achieve our result.
'''

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return max(x + y for x, y in zip(sorted(nums), sorted(nums)[::-1]))