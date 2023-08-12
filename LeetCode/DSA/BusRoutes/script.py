# Bus Routes -> Python3

'''
Explanation: Set dest_route as defaultdict of set and run loop for x, route on enumerated routes 
inside loop on y in route tp add x at dest_rout index y. Here we map the stop to routes and next we 
bfs from stop in queue to find all connected route. We save set of visited stops and wont double 
check for particular stop. We record all visited routes and clear route after visit. To implement 
we run loop on bfs then inside run loop on dest_rout at stop and loop again on routes at x. Check 
if not visited and perform operations for bfs and visited. 
'''

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dest_rout = collections.defaultdict(set)
        for x, route in enumerate(routes):
            for y in route:
                dest_rout[y].add(x)
        bfs = [(source, 0)]
        visited = set([source])
        for stop, bus in bfs:
            if stop == target: return bus
            for x in dest_rout[stop]:
                for y in routes[x]:
                    if y not in visited:
                        bfs.append((y, bus + 1))
                        visited.add(y)
                routes[x] = []
        return -1