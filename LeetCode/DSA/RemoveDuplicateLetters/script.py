# Remove Duplicate Letters -> Python3

'''
Explanation: Set locr as dict, stk as array and seen as set then loop on range of len s to set the 
last occurrence index of each character. Loop on range again and check if char not in seen then run 
loop while stk and its last index is greater than s at x and locr at stk last index is greater than 
x to remove stk pop from seen. Outside while loop append to stk and add to seen the value of s at 
x. Finally return stk after join.
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        locr, stk, seen = {}, [], set()
        for x in range(len(s)): locr[s[x]] = x
        for x in range(len(s)):
            if s[x] not in seen:
                while (stk and stk[-1] > s[x] and locr[stk[-1]] > x):
                    seen.remove(stk.pop())
                stk.append(s[x])
                seen.add(s[x])
        return ''.join(stk)