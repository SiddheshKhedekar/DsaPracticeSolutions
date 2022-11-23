# Kth Missing Positive Number -> Python3

'''
Explanation: Implement binary search and check in array to kth missing element.
'''

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r)//2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k