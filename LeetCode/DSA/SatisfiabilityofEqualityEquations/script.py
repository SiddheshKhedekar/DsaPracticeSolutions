# Satisfiability of Equality Equations -> Python3

'''
Explanation: Define find inside check if x is != uf[x] and set uf[x] to rec call uf[x] and at end 
return uf[x]. Inside main set uf to dict where a: a for a in string.lowercase python 2. Run loop 
a,e, _, b in equations and check if e = ‘=’ and set uf[find(a)] to find(b) and at end return not 
any(where e is not ! and find(a) = find(b) for a,e,_,b in equations).
'''

class Solution(object):
    def equationsPossible(self, equations):
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        uf = {a: a for a in string.lowercase}
        for a, e, _, b in equations:
            if e == '=': uf[find(a)] = find(b)
        return not any(e == '!' and find(a) == find(b) for a, e, _, b in equations)