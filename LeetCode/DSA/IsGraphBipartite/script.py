# Is Graph Bipartite? -> Python3

'''
Explanation: Initialise colr at empty dict then run loop on range len graph to check if x not in 
colr. Inside set color at x as 0 and check if not dfs to return False otherwise return true. Inside 
dfs run loop for x in graph at pos check if x in colr. Check if color at x is color at pos to 
return false in above else set colr at x as 1 - colr at pos then check if not dfs at x to return 
false otherwise return true.
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colr = {}
        def dfs(pos):
            for x in graph[pos]:
                if x in colr:
                    if colr[x] == colr[pos]: return False
                else:
                    colr[x] = 1 - colr[pos]
                    if not dfs(x): return False
            return True
        for x in range(len(graph)):
            if x not in colr:
                colr[x] = 0
                if not dfs(x): return False
        return True