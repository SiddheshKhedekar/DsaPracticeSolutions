# 132 Pattern -> Python3

'''
Explanation: Set stk as array and last as negative inf then loop on the array in reverse. Check if 
x is less than last to return true and then loop while stk and its last is less than x to pop stk. 
Then append x to stk and return False after loop end.
'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk, last = [], -inf
        for x in nums[::-1]:
            if x < last: return True
            while stk and stk[-1] < x: last = stk.pop()
            stk.append(x)
        return False