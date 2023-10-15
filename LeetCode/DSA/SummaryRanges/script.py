# Summary Ranges -> Python3

'''
Explanation: Set rngs as empty array then run loop for num in nums and check if not rngs or num is 
greater than rngs at -1,-1 after adding 1. Inside increment rings by empty array after , operation 
and outside if set rngs at -1, 1 to end as num after , operation. Finally return the array after 
joining after map of str and rng for all rng in rngs by using asked format.
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rngs = []
        for num in nums:
            if not rngs or num > rngs[-1][-1] + 1: rngs += [],
            rngs[-1][1:] = num,
        return ['->'.join(map(str, rng)) for rng in rngs]