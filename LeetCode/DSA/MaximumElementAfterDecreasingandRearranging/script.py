# Maximum Element After Decreasing and Rearranging -> Python3

'''
Explanation: First sort the array then set p to 0 and run loop for x in arr and inside set p to the 
min of p + 1 and x. Lastly return p, we keep p to store the prev value checking given condition.
'''

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        p = 0
        for x in arr: p = min(p + 1, x)
        return p