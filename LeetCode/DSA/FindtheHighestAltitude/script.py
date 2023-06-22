# Find the Highest Altitude -> Python3

'''
Explanation: Return the max of 0 and the max of accumulate on gain.
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))