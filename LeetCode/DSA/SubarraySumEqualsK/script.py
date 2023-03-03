# Subarray Sum Equals K -> Python3

'''
Explanation: Initialise res and prefixsum along with memory. Loop on nums an increment prefixsum. 
Check if prefixsum minus k in memory and increment res by mem at prefixsum minus k and if ps not in 
mem then set mem at ps to 1 else increment mem at ps value by 1.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, ps, mem = 0, 0, {0: 1}
        for n in nums:
            ps = ps + n
            if ps - k in mem: res += mem[ps - k]
            if ps not in mem: mem[ps] = 1
            else: mem[ps] = mem[ps] + 1
        return res