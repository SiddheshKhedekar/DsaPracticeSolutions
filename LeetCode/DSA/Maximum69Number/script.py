# Maximum 69 Number -> Python3

'''
Explanation: Create copy on num set index to -1 and cur to 0. While cpy run loop and check if cpy 
mod 10 is equal to 6 and set index to cur also in loop set cpy to its floor divide 10 and increment 
cur by 1. If index after loop is -1 then return num else return num + 3*10**indx.
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        cur, indx, cpy = 0, -1, num
        while cpy:
            if cpy % 10 == 6: indx = cur
            cpy, cur = cpy//10, cur+1
        return num if indx == -1 else num + 3*10**indx