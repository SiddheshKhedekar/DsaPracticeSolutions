# Minimum Time to Collect All Apples in a Tree -> Python3

'''
Explanation: Populate a array of adjacents and construct a graph. For each node check if its 
children has apples and get the cost of collecting them. Use set seen and dfs function for that.
'''

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        seen = set()
        def dfs(node):
            if node in seen: return 0
            seen.add(node)
            count = 0
            for child in graph[node]: count += dfs(child)
            if count >0: return count + 2
            return 2 if hasApple[node] else 0
        return max(dfs(0) - 2, 0)