# Buddy Strings -> Python3

'''
Explanation: Check for lengths and if not same then swap not possible also check if s and goal is 
same and len of set s is less than len of s to return true. Set diff as the array of x, y combo in 
zip s, goal where x is not same as y and return is len diff is 2 and diff at 0 is the same as 
reverse of diff at 1.
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal and len(set(s)) < len(s): return True
        diff = [(x, y) for x, y in zip(s, goal) if x != y]
        return len(diff) == 2 and diff[0] == diff[1][::-1]