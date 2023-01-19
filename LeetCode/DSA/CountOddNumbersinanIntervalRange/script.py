# Count Odd Numbers in an Interval Range -> Python3

'''
Explanation: Get the count of numbers inclusively. Check for possible combinations and values on 
condition..
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = high-low+1
        if low%2 == 1 and high%2 == 1: return int(count/2)+1
        else: return int(count/2)