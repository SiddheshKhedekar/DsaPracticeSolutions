# Number of Operations to Make Network Connected -> Python3

'''
Explanation: Check if possible condition first then initialize, populate graph and set mem to array 
of size n. then return the sum of dfs by looping in range n and subtracting 1. Inside dfs if in 
memory then return 0 otherwise set memory at x to 1 and then loop on graph x to call dfs again and 
return 1.
'''

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        graph = [set() for x in range(n)]
        for x, y in connections:
            graph[x].add(y)
            graph[y].add(x)
        mem = [0] * n
        def dfs(x):
            if mem[x]: return 0
            mem[x] = 1
            for y in graph[x]: dfs(y)
            return 1
        return sum(dfs(x) for x in range(n)) -1