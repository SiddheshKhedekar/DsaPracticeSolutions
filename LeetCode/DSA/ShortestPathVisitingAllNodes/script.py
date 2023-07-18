# Shortest Path Visiting All Nodes -> Python3

'''
Explanation: Need to start at each node and bfs to reach all other nodes. It is also necessary to 
track all visited nodes else it might loop infinitely and each node may be visited multiple times. 
Describe state using mask for each search on currentnode, visited.
'''

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nCnt, stps = len(graph), 0
        msks, allSeen = [1 << x for x in range(nCnt)], (1 << nCnt) - 1
        que = deque([(x, msks[x]) for x in range(nCnt)])
        seenStates = [{msks[x]} for x in range(nCnt)]
        while que:
            cnt = len(que)
            while cnt:
                curNode, seen = que.popleft()
                if seen == allSeen: return stps
                for nb in graph[curNode]:
                    new_seen = seen | msks[nb]
                    if new_seen == allSeen: return stps + 1
                    if new_seen not in seenStates[nb]:
                        seenStates[nb].add(new_seen)
                        que.append((nb, new_seen))
                cnt -= 1
            stps += 1
        return inf