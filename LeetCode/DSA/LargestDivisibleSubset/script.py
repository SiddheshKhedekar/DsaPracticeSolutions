# Largest Divisible Subset -> Python3

'''
Explanation: Define out as dict of -1 key with value empty set then run loop for i in sorted nums 
to assign out at i as the max where key is len of out at d for all d in out if i mod d is 0 or dict 
of i. Then at end return the list of max out values where key is len. 
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        out = {-1 : set()}
        for i in sorted(nums):
            out[i] = max((out[d] for d in out if i % d == 0), key = len) | {i}
        return list(max(out.values(), key = len))