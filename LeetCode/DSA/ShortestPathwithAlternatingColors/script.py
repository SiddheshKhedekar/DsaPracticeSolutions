# Shortest Path with Alternating Colors -> Python3

'''
Explanation: Create a graph and populate edges. Set ans to first and then max values and bfs to 
first two values. Loop bfs and loop graph inside. If ans is max val then set ans and append to bfs. 
Return array as per condition map.
'''

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for i in range(n)]
        for i, j in redEdges: graph[i][0].append(j)
        for i, j in blueEdges: graph[i][1].append(j)
        ans = [[0, 0]] + [[n*2, n*2] for i in range(n-1)]
        bfs = [[0, 0], [0, 1]]
        for i, c in bfs:
            for j in graph[i][c]:
                if ans[j][c] == n * 2:
                    ans[j][c] = ans[i][1-c] + 1
                    bfs.append([j, 1-c])
        return [x if x < n * 2 else -1 for x in map(min, ans)]