# Evaluate Division -> Python3

'''
Explanation: Define a defaultdict with dict and run for loop on tuple nm, dn and val in zip of 
equations, values. Inside set eq for index nm, nm and dn, dn as 1.0, similarly set val for index 
nm, dn and 1/val for index dn, nm. Then run another for loop on above end to loop on z in eq, 
inside loop on x in eq at z and again loop on y in eq at z, then set eq at x, y as the eq at x, z 
multiplied by eq at z, y. Finally return the array format of eq at nm by getting dn value else pass 
-1.0 for nm, dn in queries.
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], \
                     queries: List[List[str]]) -> List[float]:
        eq = collections.defaultdict(dict)
        for (nm, dn), val in zip(equations, values):
            eq[nm][nm] = eq[dn][dn] = 1.0
            eq[nm][dn] = val
            eq[dn][nm] = 1 / val
        for z in eq:
            for x in eq[z]:
                for y in eq[z]:
                    eq[x][y] = eq[x][z] * eq[z][y]
        return [eq[nm].get(dn, -1.0) for nm, dn in queries]