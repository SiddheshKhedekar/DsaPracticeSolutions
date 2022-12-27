# Largest Number At Least Twice of Others -> Python3

'''
Explanation: Loop array and get the highest and second highest number then check if condition 
applies and set index.
'''

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        high, sec, index = -1, -1, 0
        for i, n in enumerate(nums):
            if n >= high:
                sec = high
                high = n
                index = i
            elif n > sec: sec = n
        if high < sec*2: index = -1
        return index