# Find Eventual Safe States -> Python3

'''
Explanation: Move along unvisited -1 nodes and mark them as 0 on the queue while visiting others on 
the path and finish them as 1. If seen again on the queue while visiting it means you completed a 
cycle, in other words it is not safe and return back without adding.
'''

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(x):
            seen[x] = 0
            for y in graph[x]:
                if seen[y] == 0 or (seen[y] == -1 and dfs(y)): return True
            seen[x] = 1
            ans.append(x)
            return False
        seen, ans = [-1] * len(graph), []
        for x in range(len(graph)):
            if seen[x] == -1: dfs(x)
        return sorted(ans)