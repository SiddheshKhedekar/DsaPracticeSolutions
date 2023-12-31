# Trapping Rain Water -> Python3

'''
Explanation: Best solution is to implement dp using two pointers where ans, left, leftm, rightm 
set to 0 and right set to len-1. Run while loop until left is less than right. Inside check if 
value at height left is less than height right. If true check another condition if height left is 
greater than equal to leftmax. If true set lextmax to height left value else increment ans by 
leftmax - height left finally increment left. Do the same for right in the upper else decrement 
right after conditions.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        ans, left_max, right_max, left, right = 0, 0, 0, 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max: left_max = height[left]
                else: ans += left_max - height[left]
                left+=1
            else:
                if height[right] >= right_max: right_max = height[right]
                else: ans += right_max - height[right]
                right-=1
        return ans