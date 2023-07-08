# Path with Maximum Probability -> Python3

'''
Explanation: Initialize all vertices probability as 0 except for start set as 1. Then use bfs to 
traverse all reachable vertices from start, update the corresponding probabilities where we can 
have a higher probability. Otherwise ignore the vertex and when forwarding one step multiply the 
corresponding succProb value with the probability of current vertex. Repeat above till all 
probabilities reach their maximum values. Return the probability at end as solution.
'''

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], \
    start: int, end: int) -> float:
        graph, dque = defaultdict(list), deque([start])
        for z, (x, y) in enumerate(edges):
            graph[x].append([y, z])
            graph[y].append([x, z])
        prb = [0.0] * n
        prb[start] = 1.0
        while dque:
            crnt = dque.popleft()
            for nbr, z in graph.get(crnt, []):
                if prb[crnt] * succProb[z] > prb[nbr]:
                    prb[nbr] = prb[crnt] * succProb[z]
                    dque.append(nbr)
        return prb[end]