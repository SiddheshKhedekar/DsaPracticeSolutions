# Isomorphic Strings -> Python3

'''
Explanation: Inside loop using zip on both input if the current index values do not exist in the 
corresponding maps and add then to the maps. Else if the map values saved are not matching the 
values just encountered and return false.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t, t_s = {}, {}
        for i,j in zip(s,t):
            if i not in s_t and j not in t_s: s_t[i], t_s[j] = j, i
            elif s_t.get(i) != j or t_s.get(j) != i: return False
        return True