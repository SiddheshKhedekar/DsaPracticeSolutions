# Maximal Network Rank -> Python3

'''
Explanation: Save all neighbors of each node and iterate on all pairs. Create graph using 
defaultdict of set and maxnr as 0 then populate graph using a, b in roads. Loop on x in range of n 
and inside loop on y in range x to n. Then set maxnr as the max of itself and len of graph at x + 
that of y minus x in graph ay y and finally return maxnr.
'''

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph, maxNr = defaultdict(set), 0
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        for x in range(n):
            for y in range(x + 1, n):
                maxNr = max(maxNr, len(graph[x]) + len(graph[y]) - (x in graph[y]))
        return maxNr