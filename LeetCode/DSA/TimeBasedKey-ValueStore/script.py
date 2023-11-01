# Time Based Key-Value Store -> Python3

'''
Explanation: In main class init defina a ktmap using dictionary. In the set function check if key 
not in map and set ktmap key to empty array and append the timestamp value to the map at key as 
array. In the get function check if not key in map then return '' if timestamp < ktmap[key][0][0] 
then return ''. Set l and r to 0 and len(map[key]) and run loop while l < r. Inside loop set m to 
(l+r)//2. Check if map[key][m][0] < timestamp and set l to m+1 else r = m finally return '' if r == 
0 else map[key][r-1][1].
'''

class TimeMap:
    def __init__(self): self.kt_map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kt_map: self.kt_map[key] = []
        self.kt_map[key].append([timestamp,value])
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.kt_map: return ""
        if timestamp < self.kt_map[key][0][0]: return ""
        l, r = 0, len(self.kt_map[key])
        while l < r:
            m = (l + r) // 2
            if self.kt_map[key][m][0] <= timestamp: l = m + 1
            else: r = m
        return "" if r == 0 else self.kt_map[key][r-1][1]