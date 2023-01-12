# Number of Nodes in the Sub-Tree With the Same Label -> Python3

'''
Explanation: First populate a graph using edges. In the dfs function we traverse the tree and count 
the label frequency and set it in result array.
'''

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node, parent):
            cnt = Counter(labels[node])
            for child in graph.get(node, []):
                if child != parent:
                    cnt += dfs(child, node)
            res[node] = cnt[labels[node]]
            return cnt
        graph, res = defaultdict(list), [0] * n
        for i, j in edges:
            graph[i] += [j]
            graph[j] += [i]
        dfs(0,-1)
        return res