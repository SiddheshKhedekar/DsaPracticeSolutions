# Remove Max Number of Edges to Keep Graph Fully Traversable -> Python3

'''
Explanation: Go through all edges of type 3 (Alice and Bob) check if not necessary to add and 
increment res otherwise increment e1 and e2. Go through all edges of type 1 (Alice) check if not 
necessary to add and increment res otherwise increment e1. Go through all edges of type 2 (Bob) 
check if not necessary to add and increment res otherwise increment e2. If Alice's'graph is 
connected, e1 == n - 1 should valid, if Bob's graph is connected, e2 == n - 1 should valid and in 
this case we return res otherwise return -1.
'''

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(i):
            if i != root[i]: root[i] = find(root[i])
            return root[i]
        def uni(x, y):
            x, y = find(x), find(y)
            if x == y: return 0
            root[x] = y
            return 1 
        res = e1 = e2 = 0
        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if uni(i, j): e1 += 1; e2 += 1
                else: res += 1
        root0 = root[:]
        for t, i, j in edges:
            if t == 1:
                if uni(i, j): e1 += 1
                else: res += 1
        root = root0
        for t, i, j in edges:
            if t == 2:
                if uni(i, j): e2 += 1
                else: res += 1
        return res if e1 == e2 == n - 1 else -1