# Minimum Score of a Path Between Two Cities -> Python3

'''
Explanation: Initialize graph as defaultdict of dict, populate it with roads, set ans to inf, 
visited as set and dq as deque containing array of 1. While dq, popleft dq into node then loop for 
adj and scr in graph items at node index. If adj not in visited then append to deque and add to 
visited. Before end of loop set ans as the min of ans and scr.
'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        grph = defaultdict(dict)
        for i, j, x in roads: grph[i][j] = grph[j][i] = x
        ans, visited, dq = inf, set(), deque([1])
        while dq:
            node = dq.popleft()
            for adjacent, scr in grph[node].items():
                if adjacent not in visited:
                    dq.append(adjacent)
                    visited.add(adjacent)
                ans = min(ans, scr)
        return ans