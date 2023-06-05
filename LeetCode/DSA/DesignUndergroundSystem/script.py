# Design Underground System -> Python3

'''
Explanation: In init set map, totTim, cnt as dict, defaultdict, defaultdict then in checkin set map 
at id as the array of stationName, t. In checkout set m as the pop of map at id and rout as set of 
mat 0, stationName then increment totTim at route by t - m at 1 and increment cnt at route by 1. In 
getAverageTime set route as set of start and end then return totTim divided by the cnt at route.
'''

class UndergroundSystem:
    def __init__(self):
        self.map, self.routeTotTim, self.routeCnt = {}, defaultdict(int), defaultdict(int)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.map[id] = [stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        m = self.map.pop(id)
        route = (m[0], stationName)
        self.routeTotTim[route] += t - m[1]
        self.routeCnt[route] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.routeTotTim[route] / self.routeCnt[route]