# Valid Parenthesis String -> Python3

'''
Explanation: Set mn, mx as 0 then loop for x in s. Inside decrement mx if x is ‘)’ else increment 
also increment mn if x is ‘(’ else set mn as the max of mn - 1, 0 and if mx is less than 0 return 
false. Finally return if mn is 0.

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        mn = mx = 0
        for x in s:
            mx = mx - 1 if x == ')' else mx + 1
            mn = mn + 1 if x == '(' else max(mn - 1, 0)
            if mx < 0: return False
        return mn == 0