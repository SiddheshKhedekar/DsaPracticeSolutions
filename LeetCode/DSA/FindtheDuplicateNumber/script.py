# Find the Duplicate Number -> Python3

'''
Explanation: Implement pigeonhole principle and binary search. Maintain count to check how many 
nums are greater than mid and if it is more than or same as mid than that side has duplicate else 
the other and we continue to run till single element remains.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1
        while start < end:
            m, cnt = start + (end - start) // 2, 0
            for x in nums:
                if x <= m: cnt += 1
            if cnt <= m: start = m + 1
            else: end = m
        return start