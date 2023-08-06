# Similar String Groups -> Python3

'''
Explanation: Main function does a simple similarity test as per the constraints of the problem. 
Once we have this and UnionFind, we just do the O(n ^ 2 ) comparison over all nC2 strings, and if 
they are similar, then we integrate them into a group using Union.
'''

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if sum(strs[i][k] != strs[j][k] for k in range(len(strs[i]))) in (0, 2):
                    uf.union(i, j)
        return len(set(uf.find(i) for i in range(n)))

class UnionFind:
    def __init__(self, n):
        self.parent, self.rank = list(range(n)), [0 for _ in range(n)]
    def find(self, x):
        while x != self.parent[x]: x = self.parent[x]
        return x
    def union(self, x, y):
        root1, root2 = self.find(x), self.find(y)
        if root1 == root2: return
        if self.rank[root1] > self.rank[root2]: self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]: self.rank[root2] += 1