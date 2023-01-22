# Number of Provinces -> Python3

'''
Explanation: We build a graph and check if each province connected to any neighbour. For that we 
write a dfs function and use memory to keep track of all traversed neighbours.
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l, res, mem = len(isConnected), 0, set()
        def dfs(n):
            for neighbour, adjacent in enumerate(isConnected[n]):
                if adjacent and neighbour not in mem:
                    mem.add(neighbour)
                    dfs(neighbour)
        for x in range(l):
            if x not in mem:
                dfs(x)
                res += 1
        return res