# Widest Vertical Area Between Two Points Containing No Points -> Python3

'''
Explanation: Sort the xaxis points from the given array and save in temp without duplication then 
return the max diff between i and its next point in temp by looping on it.
'''

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        temp = sorted({i for i, j in points})
        return max([j - i for i, j in zip(temp, temp[1:])] + [0])