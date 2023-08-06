# Checking Existence of Edge Length Limited Paths -> Python3

'''
Explanation: Sort queries and edges based on weight then scan through queries from lowest to 
highest weight and connect the edges whose weight strictly fall below this limit. Check if the 
queried nodes p and q are connected in Union-Find structure and if so, set True in the relevant 
position otherwise set False.
'''

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: \
    List[List[int]]) -> List[bool]:
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)
        uf, ans, ii = UnionFind(n), [None] * len(queries), 0
        for w, p, q, i in queries:
            while ii < len(edgeList) and edgeList[ii][0] < w:
                _, u, v = edgeList[ii]
                uf.union(u, v)
                ii += 1
            ans[i] = uf.find(p) == uf.find(q)
        return ans

class UnionFind:
    def __init__(self, N):
        self.parent, self.rank = list(range(N)), [1] * N
    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True