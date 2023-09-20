# Minimum Fuel Cost to Report to the Capital -> Python3

'''
Explanation: Create a graph, populate paths and initialise ans write a dfs function that takes in 
graph index along with its previous and default people param. In main function call to dfs with 
base params and return ans. Inside dfs loop for all x in graph at i and check if x is prev and 
continue else increment people by dfs call of x and i. Outside loop set ans to people divide by 
seats if i else 0 and return people.
'''

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph, self.res = defaultdict(list), 0
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(i,prev, people = 1):
            for a in graph[i]:
                if a == prev: continue
                people += dfs(a, i)
            self.res += (int(ceil(people / seats)) if i else 0)
            return people
        dfs(0, 0)
        return self.res