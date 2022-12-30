# All Paths From Source to Target -> Python3

'''
Explanation: Write a dfs function and pass cur and path to it. If cur value and len graph is equal 
the append path to res else run loop on graph cur and call dfs with i and path + list i.
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path):
            if cur == len(graph) -1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path+[i])
        res = []
        dfs(0, [0])
        return res