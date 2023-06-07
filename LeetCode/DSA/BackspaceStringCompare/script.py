# Backspace String Compare -> Python3

'''
Explanation: Define search function with ans, x params and inside check if x is not # to append x 
in ans elsif ans then pop ans, then return ans and in main function return if the reduce of search 
with s, [] and t, [] are the same.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def search(ans, x):
            if x != '#': ans.append(x)
            elif ans: ans.pop()
            return ans
        return reduce(search, s, []) == reduce(search, t, [])