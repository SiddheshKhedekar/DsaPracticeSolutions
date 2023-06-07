# Time Needed to Inform All Employees -> Python3

'''
Explanation: Set chldrn as array of arrays in range n then run loop for x, mngr by enumerating 
manager. Inisde check if mngr is greater than or same as 0 to append x in chldrn at mngr. Return 
the dfs at headid and inside dfs return the max of array formed by calling dfs on y where y are 
all children at x or array of 0 after adding informTime at x.
'''

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        chldrn = [[] for _ in range(n)]
        for x, mngr in enumerate(manager):
            if mngr >= 0: chldrn[mngr].append(x)
        def dfs(x):
            return max([dfs(y) for y in chldrn[x]] or [0]) + informTime[x]
        return dfs(headID)