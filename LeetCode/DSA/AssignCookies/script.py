# Assign Cookies -> Python3

'''
Explanation: Sort both input then set child and cookie counters to 0. Loop while child and cookie 
are less then their array lengths then check if s at cookie is greatert han or same as g at child 
to increment child by 1and in all case increment cookie by 1. Finally return child at end of loop.
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]: child += 1
            cookie += 1
        return child