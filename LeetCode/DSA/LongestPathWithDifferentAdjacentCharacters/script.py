# Longest Path With Different Adjacent Characters -> Python3

'''
Explanation: Get a array of all the adjacent nodes. Dfs on each node and its children and find all 
paths starting at that node. Get the two longest paths at that node and update result.
'''

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        child, ans = [[] for _ in range(len(s))], [0]
        for x, y in enumerate(parent):
            if y >= 0: child[y].append(x)
        def dfs(x):
            candidate = [0]
            for y in child[x]:
                current = dfs(y)
                if s[x] != s[y]: candidate.append(current)
            candidate = nlargest(2,candidate)
            ans[0] = max(ans[0], sum(candidate) + 1)
            return max(candidate) + 1
        dfs(0)
        return ans[0]