# Largest 3-Same-Digit Number in String -> Python3

'''
Explanation: Compare to 2 prev values in str by looping from index 2 to end and return max value.
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max(num[x - 2:x + 1] if num[x] == num[x - 1] == num[x - 2] else '' \
        for x in range(2, len(num)))