# Rectangle Area -> Python3

'''
Explanation: Calculate the areas first. Then check for the width and height of overlapping area. If 
overlap calculate the area of overlap and subtract.
'''

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1, a2 = abs(ax2-ax1)*abs(ay1-ay2), abs(bx1-bx2)*abs(by1-by2)
        w, h = min(ax2,bx2)-max(ax1,bx1), min(ay2,by2)-max(ay1,by1)
        if w <= 0 or h <= 0: return a1+a2
        else: return a1+a2-(w*h)