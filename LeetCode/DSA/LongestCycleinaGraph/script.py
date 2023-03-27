# Longest Cycle in a Graph -> Python3

'''
Explanation: Set maxlen as -1, timestep as 1 and array of len edges with 0 value as node visited. 
Loop on the len of edges and continue if node visited at curnode is greater than 0, set start as 
timestep and i as curnode. Then loop while i is not -1 and node visited at i is equal to 0. Set 
node visited at i to timestep, i to edge at i and increment timestep by 1. If i is not -1 and node 
visited at i is greater than or same as start and set maxlen as max of it and timestep - node 
visited at i.
'''

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        lcLen, tStep, nodeVisited = -1, 1, [0] * len(edges)
        for node in range(len(edges)):
            if nodeVisited[node] > 0: continue
            startTime, i = tStep, node
            while i != -1 and nodeVisited[i] == 0:
                nodeVisited[i], i = tStep, edges[i]
                tStep += 1
            if i != -1 and nodeVisited[i] >= startTime:
                lcLen = max(lcLen, tStep - nodeVisited[i])
        return lcLen