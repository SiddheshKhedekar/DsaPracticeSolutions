# Reorganize String -> Python3

'''
Explanation: Set the least common letters at the odd indexes and put the most common letters at the 
even indexes from left to right in order of frequency. In the case some letter appears too often it 
will occupy all of the even indexes and at least the last odd index, so we need to check the last 
two indexes.
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = sorted(sorted(s), key=s.count)
        m = len(ans) // 2
        ans[1::2], ans[::2] = ans[:m], ans[m:]
        return ''.join(ans) * (ans[-1:] != ans[-2:-1])