# Container With Most Water -> Python3

'''
Explanation: Use two pointers from each end and run a while loop. Get water at current pointers and 
then check which area contains most water using max. Check for height of i and j and update loop.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, water = 0, len(height)-1, 0
        while i < j:
            water = max(water, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]: i+=1
            else: j-=1
        return water