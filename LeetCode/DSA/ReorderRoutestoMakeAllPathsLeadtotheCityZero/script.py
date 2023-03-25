# Reorder Routes to Make All Paths Lead to the City Zero -> Python3

'''
Explanation: Initialise global ans along with set of routes and graph. Populate the graph and add 
to set. Call dfs with 0 and prnt -1. Inside dfs increment ans by 1 if prnt, i in routes and run for 
loop on j in graph i then check if j is prnt and continue, before loop end call dfs again with 
child and prnt params.
'''

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.ans, routes, grph = 0, set(), defaultdict(list)
        for i, j in connections:
            routes.add((i, j))
            grph[j].append(i)
            grph[i].append(j)
        def dfs(i, prnt):
            self.ans += (prnt, i) in routes
            for j in grph[i]:
                if j == prnt: continue
                dfs(j, i)
        dfs(0, -1)
        return self.ans