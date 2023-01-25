# Increasing Triplet Subsequence -> Python3

'''
Explanation: Set two params to max int value and loop on the input to check if iteravor value less 
than the params in if and else if and finally in else return true.
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = two = float('inf')
        for i in nums:
            if i <= one: one = i
            elif i <= two: two = i
            else: return True
        return False