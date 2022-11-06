# Peak Index in a Mountain Array -> Python3

'''
Explanation: Implement binary search on array. Set low or high to middle on condition if middle and 
its next element are in ascending order.
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, h = 0, len(arr)-1
        while l < h:
            m = (l+h)//2
            if arr[m] < arr[m+1]:
                l = m+1
            else:
                h = m
        return l