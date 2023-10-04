# Reconstruct Itinerary -> Python3

'''
Explanation: Define path as empty array and dest as defaultdict of list then run loop on sorted 
tickets to append y at dest x. In visit func with ap params run loop while dest at ap and call 
visit on dest at ap pop. After loop end append ap to path and in main func call visit on ‘JFK’ then 
return the path in reverse order.
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dest, path = defaultdict(list), []
        for x, y in sorted(tickets)[::-1]: dest[x] += y,
        def visit(ap):
            while dest[ap]: visit(dest[ap].pop())
            path.append(ap)
        visit('JFK')
        return path[::-1]