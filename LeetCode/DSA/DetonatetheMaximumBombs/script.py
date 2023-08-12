# Detonate the Maximum Bombs -> Python3

'''
Explanation: Create graph using a defaultdict of list and we need to traverse all bombs starting 
from one and check if we can detonate. Loop on length of bombs and check if valid to update graph. 
Define dfs function to get seen bombs and run dfs call in for loop then save res as max of res and 
len seen.
'''

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        l, res, graph = len(bombs), 0, defaultdict(list)
        for x in range(l):
            for y in range(l):
                if x == y: continue
                if bombs[x][2]**2 >= (bombs[x][0] - bombs[y][0])**2 + (bombs[x][1] - bombs[y][1])**2:
                    graph[x] += [y]
        def dfs(node, seen):
            for chld in graph[node]:
                if chld not in seen:
                    seen.add(chld)
                    dfs(chld, seen)
        for x in range(l):
            seen = set([x])
            dfs(x, seen)
            res = max(res, len(seen))
        return res