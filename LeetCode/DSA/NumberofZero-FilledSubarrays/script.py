# Number of Zero-Filled Subarrays -> Python3

'''
Explanation: Set count, current to 0 and run loop on num. Check if number is 0 to increment current 
and then increment count by current else set current to 0.
'''

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = current = 0
        for number in nums:
            if number == 0:
                current += 1
                count += current
            else: current = 0
        return count