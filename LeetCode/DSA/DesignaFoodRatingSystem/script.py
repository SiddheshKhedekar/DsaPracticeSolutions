# Design a Food Rating System -> Python3

'''
Explanation: In init set cache as dict and mem as defaultdict of sortedlist then loop on foods, 
cuisines, ratings and set cache at f as tuple c, r then add -r, f at mem at c. In highestRated 
return mem at c 0 1 and in changeRating set c, r as cache at f then set cache at f as c, newRating 
and remove -r, f from mem at c then add -newRating, f at mem at c.
'''

from sortedcontainers import SortedList
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cache, self.mem = {}, defaultdict(SortedList)
        for f, c, r in zip(foods, cuisines, ratings):
            self.cache[f] = (c, r)
            self.mem[c].add((-r, f))
    def changeRating(self, f: str, newRating: int) -> None:
        c, r = self.cache[f]
        self.cache[f] = c, newRating
        self.mem[c].remove((-r, f))
        self.mem[c].add((-newRating, f))
    def highestRated(self, c: str) -> str: return self.mem[c][0][1]