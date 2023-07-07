# Count All Possible Routes -> Python3

'''
Explanation: Return the dfs on start and fuel after mod by given value. In cached dfs return o if 
fl is less than 0 else (1 if x is finish else 0) after adding sum of 0 if x is j else dfs on 
(j, fl - abs of locations at j - locations at x) for all j in range of len locations.
'''

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(x, fl):
            return 0 if fl < 0 else (1 if x == finish else 0) + \
            sum(0 if x == j else dfs(j, fl - abs(locations[j] - \
            locations[x])) for j in range(len(locations)))
        return dfs(start, fuel) % 1000000007