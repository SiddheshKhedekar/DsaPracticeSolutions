# Last Moment Before All Ants Fall Out of a Plank -> Python3

'''
Explanation: We can assume that when 2 ants meet they don’t change direction and keep moving in 
same direction. The max time is the max of the max of left or 0 and n - min of right or n.
'''

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left or [0]), n - min(right or [n]))