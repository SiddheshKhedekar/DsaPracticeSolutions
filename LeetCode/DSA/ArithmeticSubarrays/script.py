# Arithmetic Subarrays -> Python3

'''
Explanation: Find the min and max of each subarray, create a set of the subarray, compute the 
difference between two numbers and  check if each number is in the set. In main function loop on 
zipped l, z to get start, stop and call check on nums from start to stop. Inside helper initialize 
set and max, min. Check the len num and set condition and check if diff in max and min mod by len 
num is not 0 then set skip as max - min floor div by len nums. Loof from min to max with skips and 
check if not in set.
'''

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(num):
            seT = set(num)
            if len(num) != len(seT): return len(seT) == 1
            mX, mN = max(num), min(num)
            if (mX - mN) % (len(num) - 1) != 0: return False
            skip = (mX - mN) // (len(num) - 1)
            for x in range(mN, mX, skip):
                if x not in seT: return False
            return True
        return [check(nums[strt:stp + 1]) for strt, stp in zip(l, r)]